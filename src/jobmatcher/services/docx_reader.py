from pathlib import Path

from docx import Document


def read_docx(
    path: str | Path,
) -> str:

    document = Document(path)

    paragraphs = [
        paragraph.text
        for paragraph in document.paragraphs
    ]

    return "\n".join(paragraphs)