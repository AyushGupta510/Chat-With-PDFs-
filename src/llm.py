from langchain_ollama import ChatOllama

llm = ChatOllama(
    model ="gemma2:2b"
)

response = llm.invoke("What is AI")
print(response.content)