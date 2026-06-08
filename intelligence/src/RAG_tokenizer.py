from pathlib import Path
import os
import logging as log

from sqlalchemy.exc import SQLAlchemyError
from models.knowledge import Knowledge
from src.pdf_parser import PDFParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config.db import db
from src.sentence_embeddings import SentenceEmbeddings
from sqlalchemy.orm import Session


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

            for chunk in chunks:

                knowledge_chunk = Knowledge(
                    document_name = file.name,
                    chunk_text = chunk,
                    embedding = SentenceEmbeddings.get_embeddings(chunk)
                )
                all_chunks.append(knowledge_chunk)

        return all_chunks


    def save_chunks(self):

        engine = db.get_engine()

        try:

            chunks = self.create_chunks()

            if not chunks:
                log.warning("No chunks were generated")
                return

            with Session(engine) as session:

                try:
                    session.add_all(chunks)
                    session.commit()

                    log.info(
                        "Successfully added %d chunks",
                        len(chunks)
                    )

                except SQLAlchemyError as e:
                    session.rollback()

                    log.exception(
                        "Database error while saving chunks"
                    )

                    raise

                except Exception as e:
                    session.rollback()

                    log.exception(
                        "Unexpected error while saving chunks"
                    )

                    raise

        except FileNotFoundError as e:
            log.exception(
                "PDF directory not found"
            )

        except PermissionError as e:
            log.exception(
                "Permission denied while reading PDFs"
            )

        except ValueError as e:
            log.exception(
                "Invalid data encountered during chunk creation"
            )

        except Exception as e:
            log.exception(
                "Unexpected error during chunk processing"
            )