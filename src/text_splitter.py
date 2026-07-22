def split_text(
    text: str,
    chunk_size: int = 1200,
    chunk_overlap: int = 200,
) -> list"""
    Simple character-based text splitter.

    Good enough for a small documentation corpus.
    """
    if not text:
        return []

    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - chunk_overlap

    return chunks


def create_chunks(
    documents: list[dict],
    chunk_size: int = 1200,
    chunk_overlap: int = 200,
) -> list"""
    Converts page-level documents into smaller chunks.
    """
    all_chunks = []

    for doc in documents:
        chunks = split_text(
            doc["text"],
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

        for idx, chunk_text in enumerate(chunks, start=1):
            all_chunks.append(
                {
                    "source": doc["source"],
                    "page": doc["page"],
                    "chunk_id": idx,
                    "text": chunk_text,
                }
            )

    return all_chunks
