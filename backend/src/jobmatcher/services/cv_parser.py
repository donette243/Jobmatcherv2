from pathlib import Path
import fitz
from docx import Document

ALLOWED_EXTENSIONS = {".pdf", ".docx"}
ALLOWED_EXTENSIONS = {".pdf", ".docx"}


def parse_pdf(file_path: str) -> str:
    """
    Extract text from a PDF file.
    """
    pages_text = []

    with fitz.open(file_path) as document:
        for page in document:
            text = page.get_text()

            if text:
                pages_text.append(text)

    return "\n".join(pages_text).strip()


def parse_docx(file_path: str) -> str:
    """
    Extract text from a DOCX file.
    """
    document = Document(file_path)

    paragraphs = []

    for paragraph in document.paragraphs:
        text = paragraph.text.strip()

        if text:
            paragraphs.append(text)

    return "\n".join(paragraphs).strip()


def parse_cv(file_path: str) -> str:
    """
    Detect the file extension and extract CV text.
    """
    extension = Path(file_path).suffix.lower()

    if extension == ".pdf":
        return parse_pdf(file_path)

    if extension == ".docx":
        return parse_docx(file_path)

    raise ValueError(
        f"Unsupported file format: {extension}"
    )

