from deepagents import create_deep_agent
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from acl_rag.prompts import (
    RAG_WORKFLOW_INSTRUCTIONS,
    CHUNK_ANALYST_INSTRUCTIONS,
    SUBAGENT_DELEGATION_INSTRUCTIONS,
)
from acl_rag.tools import search_documentation, backend

max_concurrent_analysts = 3

INSTRUCTIONS = (
    RAG_WORKFLOW_INSTRUCTIONS
    + "\n\n"
    + "=" * 80
    + "\n\n"
    + SUBAGENT_DELEGATION_INSTRUCTIONS.format(
        max_concurrent_analysts=max_concurrent_analysts
    )
)

chunk_analyst_subagent = {
    "name": "chunk-analyst",
    "description": (
        "analyse one retreived documentation chunk file"
        "Pass the use question and a single file path under /retrieved/."
    ),
    "system_prompt": CHUNK_ANALYST_INSTRUCTIONS,
}


model = init_chat_model(
    model="gemini-3.6-flash",
    model_provider="google_genai",
    max_retries=5
)

agent = create_deep_agent(
    model=model,
    tools=[search_documentation],
    backend=backend,
    system_prompt=INSTRUCTIONS,
    subagents=[chunk_analyst_subagent],
)

example_query = "what is a Single Cell Protein?"

result = agent.invoke({"messages": [HumanMessage(content=example_query)]})

print(result["messages"][-1].content)