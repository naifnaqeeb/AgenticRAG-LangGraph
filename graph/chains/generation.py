from dotenv import load_dotenv
load_dotenv()

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

prompt = ChatPromptTemplate.from_template(
    """
You are an assistant for question-answering tasks.

Use the following retrieved context to answer the question.
If you don't know the answer, just say you don't know.

Question:
{question}

Context:
{context}

Answer:
"""
)

generation_chain = prompt | llm | StrOutputParser()