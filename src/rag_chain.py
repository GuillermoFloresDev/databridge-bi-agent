import os

from dotenv import load_dotenv

from src.cohere_client import get_cohere_client, get_chat_model
from src.prompts import SYSTEM_PROMPT, build_user_prompt
from src.retriever import retrieve


load_dotenv()


def answer_question(question: str) -> dict:
    """
    Full RAG flow:
    - retrieve chunks
    - build prompt
    - call Cohere Chat
    - return answer and sources
    """
    top_k = int(os.getenv("TOP_K", "5"))

    chunks = retrieve(question, top_k=top_k)

    user_prompt = build_user_prompt(question, chunks)

    co = get_cohere_client()

    response = co.chat(
        model=get_chat_model(),
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
    )

    answer = response.message.content[0].text

    sources = [
        {
            "source": chunk["source"],
            "page": chunk["page"],
            "score": round(chunk["score"], 4),
        }
        for chunk in chunks
    ]

    return {
        "answer": answer,
        "sources": sources,
    }
