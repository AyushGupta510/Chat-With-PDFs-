from src.splitter import chunks
from src.embedding import embeddings
from langchain_community.vectorstores import FAISS
import os

if os.path.exists("faiss_index"):

    vectorstore = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    print("Loaded Existing FAISS")

else:

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    vectorstore.save_local("faiss_index")

    print("Created New FAISS")