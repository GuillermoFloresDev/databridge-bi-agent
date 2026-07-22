import json
from pathlib import Path

import numpy as np

from src.document_loader import load_documents_from_folder
from src.text_splitter import create_chunks
from src.cohere_client import get_cohere_client, get_embed_model


DOCS_DIR = "docs"
STORAGE_DIR = Path("storage")
CHUNKS_PATH = STORAGE_DIR / "chunks.json"
EMBEDDINGS_PATH = STORAGE_DIR / "embeddings.npy"


def embed_documents(texts: list[str], batch_size: int = 32) -> np.ndarray:
    """
    Creates document embeddings with Cohere in batches.
    """
    co = get_cohere_client()
    all_embeddings = []

    for start in range(0, len(texts), batch_size):
        batch = texts[start : start + batch_size]

        print(
            f"Embedding batch {start // batch_size + 1} "
            f"({start + len(batch)}/{len(texts)})"
        )

        response = co.embed(
            model=get_embed_model(),
            input_type="search_document",
            texts=batch,
            embedding_types=["float"],
        )

        all_embeddings.extend(response.embeddings.float)

    return np.array(all_embeddings, dtype=np.float32)


def main():
    print("Loading PDF documents...")
    documents = load_documents_from_folder(DOCS_DIR)

    print(f"Loaded {len(documents)} PDF pages with text.")

    print("Creating text chunks...")
    chunks = create_chunks(
        documents,
        chunk_size=1200,
        chunk_overlap=200,
    )

    print(f"Created {len(chunks)} chunks.")

    STORAGE_DIR.mkdir(exist_ok=True)

    texts = [chunk["text"] for chunk in chunks]

    print("Creating embeddings with Cohere...")
    embeddings = embed_documents(texts)

    print("Saving chunks and embeddings...")

    with open(CHUNKS_PATH, "w", encoding="utf-8") as file:
        json.dump(chunks, file, ensure_ascii=False, indent=2)

    np.save(EMBEDDINGS_PATH, embeddings)

    print("Index created successfully.")
    print(f"Chunks: {CHUNKS_PATH}")
    print(f"Embeddings: {EMBEDDINGS_PATH}")


if __name__ == "__main__":
    main()