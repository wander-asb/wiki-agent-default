from langchain_core.prompts import ChatPromptTemplate

qa_prompt = ChatPromptTemplate.from_template(
    "You are an assistant. Use the following context to answer the question.\n\n"
    "Context:\n{context}\n\n"
    "Question:\n{question}"
)