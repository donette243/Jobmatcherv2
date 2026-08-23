from jobmatcher.services.cv_reader import read_cv
from jobmatcher.services.skill_extractor import extract_skills


def test_extract_cv_and_skills(cv_file):
    text = read_cv(str(cv_file))

    assert text is not None
    assert len(text) > 0

    skills = extract_skills(text)

    assert isinstance(skills, list)
    assert len(skills) > 0