import re


CV_SECTION_KEYWORDS = {
    "experience",
    "work experience",
    "professional experience",
    "employment",
    "education",
    "skills",
    "technical skills",
    "projects",
    "certifications",
    "languages",
    "summary",
    "profile",
    "expérience",
    "expérience professionnelle",
    "formation",
    "compétences",
    "projets",
    "certifications",
    "langues",
    "profil",
    "опыт",
    "опыт работы",
    "образование",
    "навыки",
    "профессиональные навыки",
    "проекты",
    "сертификаты",
    "языки",
    "о себе",
}

CONTACT_PATTERNS = [
    r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",
    r"(?:\+?\d[\d\s().-]{7,}\d)",
    r"(?:linkedin\.com/in/)",
    r"(?:github\.com/)",
]

DATE_RANGE_PATTERNS = [
    r"\b(?:19|20)\d{2}\s*[-–—]\s*(?:(?:19|20)\d{2}|present|current|now)\b",
    r"\b(?:19|20)\d{2}\s*[-–—]\s*(?:настоящее время|н\.?\s*в\.?)\b",
    r"\b(?:19|20)\d{2}\s*[-–—]\s*(?:présent|aujourd'hui|aujourd’hui)\b",
]


def _count_section_keywords(text: str) -> int:
    text_lower = text.lower()

    return sum(
        1
        for keyword in CV_SECTION_KEYWORDS
        if re.search(
            rf"(?<!\w){re.escape(keyword)}(?!\w)",
            text_lower,
        )
    )


def _has_contact_information(text: str) -> bool:
    return any(
        re.search(
            pattern,
            text,
            flags=re.IGNORECASE,
        )
        for pattern in CONTACT_PATTERNS
    )


def _has_date_range(text: str) -> bool:
    return any(
        re.search(
            pattern,
            text,
            flags=re.IGNORECASE,
        )
        for pattern in DATE_RANGE_PATTERNS
    )


def is_likely_cv(text: str) -> bool:
    if not text or len(text.strip()) < 100:
        return False

    section_count = _count_section_keywords(text)
    has_contact = _has_contact_information(text)
    has_date_range = _has_date_range(text)

    score = 0

    if section_count >= 2:
        score += 2

    if section_count >= 4:
        score += 1

    if has_contact:
        score += 2

    if has_date_range:
        score += 1

    return score >= 4


def validate_cv(text: str) -> None:
    if not is_likely_cv(text):
        raise ValueError(
            "The uploaded document does not appear to be a CV."
        )