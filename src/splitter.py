from src.loader import docs
from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = text_splitter.split_documents(docs)

print("CHUNKS OF THAT PAGE CONTENT:")
print(chunks[0].page_content[:300])
print("CHUNKS:")
print(len(chunks))
print(type(chunks))
print(type(chunks[0]))