# ACL RAG with LangChain

RAG LangChain Chatbot feed by your documents.
I am ussing HuggingFaceEmbeddings instead of openai emdedings to save tokens 💸

## Run

```bash
uv run streamlit run src/acl_rag/main.py
```

## DEV
do not forget 
```bash
source .venv/bin/activate
```
and 
```bash
ollama run qwen3:1.7b
```
