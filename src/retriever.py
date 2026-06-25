from src.vectorstore import vectorstore
retriever = vectorstore.as_retriever(
    search_kwargs = {"k":3}
)
query = "what is self - attention"
docs = retriever.invoke(query)
for i, doc in enumerate(docs):
    print(f"\nResult {i+1}")
    print(doc.page_content[:300])