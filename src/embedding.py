from src.splitter import chunks
from langchain_ollama import OllamaEmbeddings
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

vector = embeddings.embed_documents(
    [chunk.page_content for chunk in chunks]
)
print("Total Chunks:", len(chunks))
print("Total Vectors:", len(vector))
print("Vector Dimension:", len(vector[0]))