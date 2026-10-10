from pathlib import Path
from typing import List
from langchain_core.documents import Document
from pypdf import PdfReader


def read_pdf_text(pdf_path: str | Path) -> str:
    path = Path(pdf_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    reader = PdfReader(str(path))