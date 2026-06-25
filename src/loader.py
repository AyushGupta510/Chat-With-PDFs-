from langchain_community.document_loaders import PyPDFLoader

def load_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    return loader.load()

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