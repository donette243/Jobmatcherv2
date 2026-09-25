from jobmatcher.models.job import Job
from jobmatcher.models.profile import Profile
from jobmatcher.models.skill import Skill
from jobmatcher.services.matching_service import (
    calculate_match_score,
)


def test_calculate_match_score():
    profile = Profile(
        id=1,
        user_id=1,
        name="John Doe",
        experience_years=10,
    )

    profile.skills = [
        Skill(name="python"),
        Skill(name="javascript"),
        Skill(name="docker"),
        Skill(name="kubernetes"),
    ]

    job = Job(
        id=1,
        title="Software Engineer",
        company="Google",
        location="San Francisco, CA",
        description=(
            "We are looking for a software engineer "
            "with experience in Python and JavaScript"
        ),
        source="LinkedIn",
        remote=False,
    )

    job.skills = [
        Skill(name="python"),
        Skill(name="javascript"),
    ]

    score = calculate_match_score(
        profile,
        job,
    )

    assert score == 100.0