from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_template(
"""
You are a helpful AI assistant.

Answer the question using ONLY the provided context.

If the answer is not present in the context, say:
"I couldn't find the answer in the provided document."

Context:
{context}

Question:
{question}

Answer:
"""
)