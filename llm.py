from langchain_community.chat_models import ChatOllama
import config

llm = ChatOllama(
    model=config.MODEL_NAME,
    temperature=0
)

def generate_answer(query, docs):
    if not docs:
        return "I don't know"

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an intelligent customer support assistant.

Rules:
- Answer ONLY from the context
- If unsure, say "I don't know"
- Be concise and helpful

Context:
{context}

Question:
{query}

Answer:
"""

    return llm.invoke(prompt).content