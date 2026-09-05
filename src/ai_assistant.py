import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()


def ask_ai(question, summary):

    api_key = os.getenv("GOOGLE_API_KEY")


    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=api_key,
        temperature=0.3
    )


    context = f"""
You are an AI Business Analyst.

Analyze the sales information below and answer the user's question.

Sales Summary:

{summary}


User Question:

{question}

Give a clear business explanation.
"""


    response = llm.invoke(context)

    return response.content