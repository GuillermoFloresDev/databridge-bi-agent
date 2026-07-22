import os
import cohere
from dotenv import load_dotenv


load_dotenv()


def get_cohere_client() -> cohere.ClientV2:
    """
    Creates a Cohere ClientV2 using COHERE_API_KEY.
    """
    api_key = os.getenv("COHERE_API_KEY") or os.getenv("CO_API_KEY")

    if not api_key:
        raise ValueError(
            "Missing COHERE_API_KEY. Add it to your .env file."
        )

    return cohere.ClientV2(api_key=api_key)


def get_embed_model() -> str:
    return os.getenv("COHERE_EMBED_MODEL", "embed-v4.0")


def get_chat_model() -> str:
    return os.getenv("COHERE_CHAT_MODEL", "command-r-plus-08-2024")
