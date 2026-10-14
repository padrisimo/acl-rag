from pathlib import Path
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_huggingface import HuggingFaceEmbeddings 
from langchain_text_splitters import RecursiveCharacterTextSplitter
from acl_rag.filereader import read_pdf_documents

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

vector_store = InMemoryVectorStore(embeddings)

DOC_PATHS = [
    "src/data/ajol.pdf",
    "src/data/single-cell-protein.pdf",
]

docs = read_pdf_documents(DOC_PATHS)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

all_splits = text_splitter.split_documents(docs)
print(f"Number of chunks: {len(all_splits)}")

vector_store.add_documents(documents=all_splits)
print(f"indexed {len(all_splits)} chunks in the vector store.")
