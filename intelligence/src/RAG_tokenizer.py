from pathlib import Path
import os
from src.pdf_parser import PDFParser
from langchain.text_splitter import RecursiveCharacterTextSplitter

class RAGTokenizer:

    base_path = ""
    folder_path = ""
    tmp_path = "tmp"
    def __init__(self):
        self.base_path = Path(__path__).parent.parent
        self.folder_path = os.path.join(self.base_path,self.tmp_path)

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