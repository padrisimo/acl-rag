from pathlib import Path
from typing import List
from langchain_core.documents import Document
from pypdf import PdfReader


def read_pdf_text(pdf_path: str | Path) -> str:
    path = Path(pdf_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    reader = PdfReader(str(path))
    text_parts = [page.extract_text() or "" for page in reader.pages]
    return "\n".join(text_parts)


def read_pdf_documents(pdf_paths: List[str | Path]) -> List[Document]:
    documents: List[Document] = []
    for path in pdf_paths:
        path_obj = Path(path)
        text = read_pdf_text(path_obj)
        documents.append(
            Document(page_content=text, metadata={"source": str(path_obj)})
        )
    return documents

