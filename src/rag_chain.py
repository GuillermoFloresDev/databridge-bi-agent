import os

from dotenv import load_dotenv

from src.cohere_client import get_cohere_client, get_chat_model
from src.prompts import SYSTEM_PROMPT, build_user_prompt
from src.retriever import retrieve
from src.query_classifier import is_greeting_or_smalltalk, is_too_short


load_dotenv()


MIN_RELEVANCE_SCORE = float(os.getenv("MIN_RELEVANCE_SCORE", "0.23"))


def answer_question(question: str) -> dict:
    """
    Full RAG flow:
    - detect greetings and short queries
    - retrieve chunks
    - validate relevance
    - build prompt
    - call Cohere Chat
    - return answer and sources
    """

    if is_greeting_or_smalltalk(question):
        return {
            "answer": (
                "¡Hola! Soy DataBridge BI Assistant. "
                "Puedo ayudarte a consultar la documentación interna de DataBridge BI Solutions. "
                "Por ejemplo, puedes preguntarme sobre medidas DAX, incidentes BI, arquitectura analítica, "
                "onboarding, ingeniería de datos o servicios y SLAs."
            ),
            "sources": [],
        }

    if is_too_short(question):
        return {
            "answer": (
                "Tu consulta es muy breve. Por favor, escribe una pregunta más específica sobre la documentación. "
                "Por ejemplo: ¿Cómo deben nombrarse las medidas DAX? o ¿Qué se considera un incidente SEV-1?"
            ),
            "sources": [],
        }

    top_k = int(os.getenv("TOP_K", "5"))

    chunks = retrieve(question, top_k=top_k)

    if not chunks:
        return {
            "answer": (
                "No encontré información relevante en la documentación de DataBridge BI Solutions "
                "para responder esta pregunta."
            ),
            "sources": [],
        }

    best_score = chunks[0]["score"]

    if best_score < MIN_RELEVANCE_SCORE:
        return {
            "answer": (
                "No encontré suficiente evidencia en la documentación para responder con confianza. "
                "Intenta formular la pregunta con más detalle o usando términos relacionados con BI, "
                "Power BI, DAX, ingeniería de datos, incidentes, arquitectura o servicios."
            ),
            "sources": [
                {
                    "source": chunk["source"],
                    "page": chunk["page"],
                    "score": round(chunk["score"], 4),
                }
                for chunk in chunks
            ],
        }

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