from pathlib import Path

from sqlalchemy.orm import Session

from jobmatcher.schemas.user import UserRead
from jobmatcher.services.cv_parser import parse_cv
from jobmatcher.services.profile_service import (
    create_or_update_profile,
)
from jobmatcher.services.profile_extractor import extract_profile
from jobmatcher.schemas.profile import ProfileExtract


def process_cv(
    db: Session,
    user: UserRead,
    path: str | Path,
):

    parsed = parse_cv(path)

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
