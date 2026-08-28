import re
from jobmatcher.schemas.profile import ProfileExtract

SKILLS = {
    "python": "Python",
    "java": "Java",
    "javascript": "JavaScript",
    "typescript": "TypeScript",
    "c#": "C#",
    "c++": "C++",
    "php": "PHP",
    "go": "Go",
    "rust": "Rust",
    "sql": "SQL",
    "mysql": "MySQL",
    "postgresql": "PostgreSQL",
    "mongodb": "MongoDB",
    "redis": "Redis",
    "docker": "Docker",
    "kubernetes": "Kubernetes",
    "git": "Git",
    "linux": "Linux",
    "fastapi": "FastAPI",
    "django": "Django",
    "flask": "Flask",
    "tensorflow": "TensorFlow",
    "pytorch": "PyTorch",
    "keras": "Keras",
    "scikit-learn": "Scikit-learn",
    "pandas": "Pandas",
    "numpy": "NumPy",
    "opencv": "OpenCV",
    "transformers": "Transformers",
    "machine learning": "Machine Learning",
    "deep learning": "Deep Learning",
    "natural language processing": "Natural Language Processing",
    "nlp": "NLP",
    "computer vision": "Computer Vision",
    "data analysis": "Data Analysis",
}
def extract_skills(text: str) -> list[str]:
    text_lower = text.lower()

    found_skills = set()

    for keyword, skill_name in SKILLS.items():
        pattern = rf"(?<!\w){re.escape(keyword)}(?!\w)"

        if re.search(pattern, text_lower):
            found_skills.add(skill_name)

    return sorted(found_skills)
LANGUAGES = {
    "french": "French",
    "français": "French",
    "english": "English",
    "anglais": "English",
    "russian": "Russian",
    "русский": "Russian",
    "german": "German",
    "allemand": "German",
    "spanish": "Spanish",
    "espagnol": "Spanish",
}
def extract_languages(text: str) -> list[str]:
    text_lower = text.lower()

    found_languages = set()

    for keyword, language in LANGUAGES.items():
        if keyword in text_lower:
            found_languages.add(language)

    return sorted(found_languages)
POSITIONS = {
    "backend developer": "Backend Developer",
    "backend engineer": "Backend Engineer",
    "software engineer": "Software Engineer",
    "software developer": "Software Developer",
    "python developer": "Python Developer",
    "data analyst": "Data Analyst",
    "data scientist": "Data Scientist",
    "machine learning engineer": "Machine Learning Engineer",
    "ml engineer": "Machine Learning Engineer",
    "devops engineer": "DevOps Engineer",
    "frontend developer": "Frontend Developer",
    "full stack developer": "Full Stack Developer",
}
def extract_desired_positions(text: str) -> list[str]:
    text_lower = text.lower()

    positions = set()

    for keyword, position in POSITIONS.items():
        if keyword in text_lower:
            positions.add(position)

    return sorted(positions)
def extract_name(text: str) -> str | None:
    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    if not lines:
        return None

    first_line = lines[0]

    if len(first_line.split()) <= 4:
        return first_line

    return None
def extract_experience_years(
    text: str,
) -> float | None:

    patterns = [
        r"(\d+(?:[.,]\d+)?)\s*\+?\s*years?\s+(?:of\s+)?experience",
        r"(\d+(?:[.,]\d+)?)\s*\+?\s*ans?\s+d['’]expérience",
    ]

    for pattern in patterns:
        match = re.search(
            pattern,
            text,
            flags=re.IGNORECASE,
        )

        if match:
            value = match.group(1).replace(",", ".")

            return float(value)

    return None
EDUCATION_KEYWORDS = [
    "master",
    "bachelor",
    "licence",
    "phd",
    "doctorate",
    "doctorat",
    "магистратура",
    "бакалавр",
    "аспирантура",
]
def extract_education(text: str) -> list[str]:
    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    education = []

    for line in lines:
        line_lower = line.lower()

        if any(
            keyword in line_lower
            for keyword in EDUCATION_KEYWORDS
        ):
            education.append(line)

    return education


def extract_profile(text: str) -> ProfileExtract:
    return ProfileExtract(
        name=extract_name(text),
        skills=extract_skills(text),
        languages=extract_languages(text),
        education=extract_education(text),
        desired_positions=extract_desired_positions(text),
        experience_years=extract_experience_years(text),
    )
