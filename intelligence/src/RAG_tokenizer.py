from pathlib import Path
import os
import psycopg2
from psycopg2.extras import execute_batch
from src.pdf_parser import PDFParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config.db import db


class RAGTokenizer:

    base_path = ""
    folder_path = ""
    tmp_path = "tmp"

    def __init__(self):

        self.base_path = Path(__file__).parent.parent

        self.folder_path = os.path.join(
            self.base_path,
            self.tmp_path
        )

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

    def create_chunks(self):

        files = [
            f for f in Path(self.folder_path).iterdir()
            if f.is_file() and f.suffix.lower() == ".pdf"
        ]

        parser = PDFParser()

        all_chunks = []

        for file in files:

            text = parser.extract_pdf_content(file)

            chunks = self.splitter.split_text(text)

            for i, chunk in enumerate(chunks):

                all_chunks.append({
                    "document": file.name,
                    "chunk_id": i,
                    "text": chunk
                })

        return all_chunks

    def save_chunks(self):

        conn = db.get_connection()

        try:

            cur = conn.cursor()

            chunks = self.create_chunks()

            query = """
                INSERT INTO document_chunks
                (
                    document_name,
                    chunk_id,
                    chunk_text
                )
                VALUES (%s, %s, %s)
            """

            values = [
                (
                    chunk["document"],
                    chunk["chunk_id"],
                    chunk["text"]
                )
                for chunk in chunks
            ]

            execute_batch(cur, query, values)

            conn.commit()

            print("Chunks saved successfully")

        except Exception as e:

            conn.rollback()

            print("Error:", e)

        finally:

            db.release_connection(conn)