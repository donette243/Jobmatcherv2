from pathlib import Path

from sqlalchemy.orm import Session

from jobmatcher.models.user import User
from jobmatcher.services.cv_parser import parse_cv
from jobmatcher.services.cv_validator import validate_cv
from jobmatcher.services.profile_extractor import extract_profile
from jobmatcher.services.profile_service import (
    create_or_update_profile,
)


def process_cv(
    db: Session,
    user: User,
    path: str | Path,
):
    parsed = parse_cv(path)

    validate_cv(parsed)

    profile_data = extract_profile(parsed)

    profile = create_or_update_profile(
        db=db,
        user=user,
        name=profile_data.name,
        experience_years=profile_data.experience_years,
        skills=profile_data.skills,
        languages=profile_data.languages,
        education=profile_data.education,
        desired_positions=profile_data.desired_positions,
    )

    return profile, parsed