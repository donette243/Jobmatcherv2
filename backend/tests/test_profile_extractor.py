from jobmatcher.services.profile_extractor import extract_profile


def test_extract_profile():
    text = """
    Donet Kuba

    Python Backend Developer

    Skills:
    Python
    SQL
    Docker
    FastAPI
    PostgreSQL

    I have 3 years of experience.

    Languages:
    French
    English
    Russian

    Master Software Engineering
    """

    profile = extract_profile(text)

    assert "python" in [skill.lower() for skill in profile.skills]
    assert "sql" in [skill.lower() for skill in profile.skills]
    assert "docker" in [skill.lower() for skill in profile.skills]
    assert "fastapi" in [skill.lower() for skill in profile.skills]

    assert "French" in profile.languages
    assert "English" in profile.languages
    assert "Russian" in profile.languages

    assert profile.experience_years == 3
