import pypdfium2 as pdfium
from pathlib import Path
import time

class PDFParser:
    
    def extract_pdf_content(self,file):
        content = "\n".join(
            p.get_textpage().get_text_range() 
                for p in pdfium.PdfDocument(file)
        )
        return content
