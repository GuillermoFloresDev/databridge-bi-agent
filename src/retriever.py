import json
from pathlib import Path

import numpy as np

from src.cohere_client import get_cohere_client, get_embed_model


STORAGE_DIR = Path("storage")
CHUNKS_PATH = STORAGE_DIR / "chunks.json"
EMBEDDINGS_PATH = STORAGE_DIR / "embeddings.npy"


def load_index() -> tuple[list[dict], np.ndarray]:
    """
    Loads chunks and embeddings from local storage.
    """
    if not CHUNKS_PATH.exists() or not EMBEDDINGS_PATH.exists():
        raise FileNotFoundError(
            "Index not found. Run: python build_index.py"
        )

    with open(CHUNKS_PATH, "r", encoding="utf-8") as file:
        chunks = json.load(file)

    embeddings = np.load(EMBEDDINGS_PATH)

    return chunks, embeddings


def normalize_vectors(vectors: np.ndarray) -> np.ndarray:
    """
    Normalizes vectors for cosine similarity.
    """
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    norms[norms == 0] = 1
    return vectors / norms


def embed_query(query: str) -> np.ndarray:
    """
    Creates a query embedding with Cohere.
    """
    co = get_cohere_client()

    response = co.embed(
        model=get_embed_model(),
        input_type="search_query",
        texts=[query],
        embedding_types=["float"],
    )

    return np.array(response.embeddings.float, dtype=np.float32)


def retrieve(query: str, top_k: int = 5) -> list"""
    Retrieves the most relevant chunks for a query.
    """
    chunks, doc_embeddings = load_index()

    query_embedding = embed_query(query)

    doc_embeddings = normalize_vectors(doc_embeddings)
    query_embedding = normalize_vectors(query_embedding)

    scores = np.dot(query_embedding, doc_embeddings.T)[0]
    top_indices = np.argsort(-scores)[:top_k]

    results = []

    for idx in top_indices:
        item = chunks[int(idx)].copy()
        item["score"] = float(scores[int(idx)])
        results.append(item)

    return results
