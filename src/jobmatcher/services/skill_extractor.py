import re


DEFAULT_SKILLS = {
    "python",
    "java",
    "javascript",
    "typescript",
    "c#",
    "c++",
    "php",
    "sql",
    "mysql",
    "postgresql",
    "fastapi",
    "django",
    "flask",
    "docker",
    "kubernetes",
    "git",
    "linux",
    "tensorflow",
    "pytorch",
    "keras",
    "opencv",
    "pandas",
    "numpy",
    "scikit-learn",
    "machine learning",
    "data analysis",
    "rest api",
    "aws",
    "azure",
}


def normalize_skill(
    skill: str,
) -> str:

    return re.sub(
        r"\s+",
        " ",
        skill.strip().lower(),
    )


def extract_skills(
    text: str,
    skills: set[str] | None = None,
) -> list[str]:

    catalog = skills or DEFAULT_SKILLS

    normalized_text = text.lower()

    found = set()

    for skill in catalog:

        pattern = (
            r"(?<!\w)"
            + re.escape(skill.lower())
            + r"(?!\w)"
        )

        if re.search(
            pattern,
            normalized_text,
        ):
            found.add(
                normalize_skill(skill)
            )

    return sorted(found)