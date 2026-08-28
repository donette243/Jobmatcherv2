from pathlib import Path
from jobmatcher.services.docx_reader import read_docx
from jobmatcher.services.pdf_reader import read_pdf


def read_cv(
    path: str | Path,
) -> str:

    path = Path(path)

    extension = path.suffix.lower()

    if extension == ".pdf":
        return read_pdf(path)

    if extension == ".docx":
        return read_docx(path)

    raise ValueError(
        "Unsupported CV format. "
        "Only PDF and DOCX are supported."
    )


def extract_cv_text(
    path: str | Path,
) -> str:
    return read_cv(path)