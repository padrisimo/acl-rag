# ACL RAG with LangChain

RAG LangChain Chatbot feed by your documents.
I am ussing HuggingFaceEmbeddings instead of openai emdedings to save tokens 💸

### Run

```bash
uv run streamlit run src/acl_rag/main.py
```

### DEV

create virtual enviroment
```bash
uv venv --python 3.12
```
activate
```bash
source .venv/bin/activate
```
run local model 
```bash
ollama run qwen3:1.7b
```
