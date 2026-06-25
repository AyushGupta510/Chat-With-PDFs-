import streamlit as st

from src.retriever import retriever
from src.prompt import prompt
from src.llm import llm

# Page Title
st.set_page_config(
    page_title="Chat With PDF",
    page_icon="📄"
)

st.title("📄 Chat With PDF")

question = st.text_input(
    "Ask a question about the PDF:"
)

if question:

    # Retrieve relevant chunks
    docs = retriever.invoke(question)

    # Create context
    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    # Create prompt
    final_prompt = prompt.invoke(
        {
            "context": context,
            "question": question
        }
    )

    # Generate answer
    response = llm.invoke(final_prompt)

    # Display answer
    st.subheader("Answer")
    st.write(response.content)

    # Show retrieved chunks
    with st.expander("Retrieved Chunks"):
        for i, doc in enumerate(docs):
            st.write(f"### Chunk {i+1}")
            st.write(doc.page_content[:500])

from src.loader import load_pdf

uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

if uploaded_file:

    file_path = f"data/{uploaded_file.name}"

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    docs = load_pdf(file_path)