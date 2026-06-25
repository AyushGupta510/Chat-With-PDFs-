from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("data/AI_Article.pdf")
docs = loader.load()

# print("\n Type of Docs:")
# print(type(docs))

# print("\n first Document:")
# print(docs[0])

# print("\n First texts of document")
# print(docs[0].page_content[:500])

# print("\n Metadata:")
# print(docs[0].metadata)

# print("\n length of Document:")
# print(len(docs))