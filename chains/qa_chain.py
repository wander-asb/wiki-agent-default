from langchain_together import ChatTogether
from prompt.qa_prompt import qa_prompt

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("TOGETHER_API_KEY")

llm = ChatTogether(
    model="meta-llama/Llama-3-8b-chat-hf",
    together_api_key=api_key
)

qa_chain = qa_prompt | llm
