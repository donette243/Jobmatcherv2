from pathlib import Path

import fitz


def read_pdf(
    path: str | Path,
) -> str:

    document = fitz.open(path)

    try:
        pages = [
            page.get_text()
            for page in document
        ]

        return "\n".join(pages)

    finally:
        document.close()