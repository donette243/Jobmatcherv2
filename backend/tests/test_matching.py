from jobmatcher.schemas.profile import ProfileRead
from jobmatcher.schemas.job import JobData
from jobmatcher.services.matching_service import (
    calculate_match_score,
)


def test_calculate_match_score():
    profile = ProfileRead(
        id=1,
        user_id=1,
        name="John Doe",
        experience_years=10,
        skills=["Python", "JavaScript", "Docker", "Kubernetes"],
        languages=["English", "Spanish"],
        education=["Bachelor's degree in Computer Science"],
        desired_positions=["Software Engineer"],
    )
    job = JobData(
        title="Software Engineer",
        company="Google",
        location="San Francisco, CA",
        description="We are looking for a software engineer with 10 years of experience in Python and JavaScript",
        source="LinkedIn",
    )
    score = calculate_match_score(profile, job)
    print(score)