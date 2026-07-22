from pathlib import Path
from pypdf import PdfReader


def load_pdf_text(pdf_path: Path) -> list[dict]:
    """
    Extracts text page by page from a PDF.

    Returns a list of dictionaries with:
    - source
   - text
    """
    reader = PdfReader(str(pdf_path))
    pages = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        text = text.strip()

        if text:
            pages.append(
                {
                    "source": pdf_path.name,
                    "page": page_number,
                    "text": text,
                }
            )

    return pages


def load_documents_from_folder(folder_path: str = "docs") -> list"""
    Loads all PDF files from the docs folder.
    """
    folder = Path(folder_path)

    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder_path}")

    pdf_files = sorted(folder.glob("*.pdf"))

    if not pdf_files:
        raise FileNotFoundError(f"No PDF files found in: {folder_path}")

    documents = []

    for pdf_file in pdf_files:
        documents.extend(load_pdf_text(pdf_file))

    return documents
