def is_greeting_or_smalltalk(query: str) -> bool:
    """
    Detects greetings or small talk that should not trigger RAG retrieval.
    """
    normalized = query.strip().lower()

    greetings = {
        "hola",
        "buenas",
        "buenos días",
        "buenos dias",
        "buenas tardes",
        "buenas noches",
        "hey",
        "hello",
        "hi",
        "qué tal",
        "que tal",
        "saludos",
    }

    return normalized in greetings


def is_too_short(query: str) -> bool:
    """
    Detects very short queries that are unlikely to be valid documentation questions.
    """
    normalized = query.strip()

    if len(normalized) < 8:
        return True




    words = normalized.split()

    return len(words) < 2