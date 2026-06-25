from retriever import retriever
from llm import llm
from prompt import prompt

query= input("Ask a question: ")

# Step 1: Retrieve relevant chunks
docs = retriever.invoke(query)

# Step 2: Create context
context = "\n\n".join(
    [doc.page_content for doc in docs]
)

# Step 3: Fill prompt template
final_prompt = prompt.invoke(
    {
        "context": context,
        "question": query
    }
)

# Step 4: Send to LLM
response = llm.invoke(final_prompt)

# Step 5: Print answer
print("\nAnswer:\n")
print(response.content)