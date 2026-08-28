from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from jobmatcher.auth.dependencies import get_current_user
from jobmatcher.database.dependencies import get_db
from jobmatcher.models.user import User
from jobmatcher.schemas.profile import PreferenceCreate, ProfileCreate
from jobmatcher.services.preference_service import (
    create_or_update_preferences,
)
from jobmatcher.services.profile_service import (
    create_or_update_profile,
    get_profile,
)

router = APIRouter(
    prefix="/profile",
    tags=["Profile"],
)


@router.get("")
def read_profile(
    db: Annotated[Session, Depends(get_db)],
    user: Annotated[User, Depends(get_current_user)],
):
    profile = get_profile(db, user.id)

    if profile is None:
        raise HTTPException(
            status_code=404,
            detail="Profile not found",
        )

    return {
        "id": profile.id,
        "user_id": profile.user_id,
        "name": profile.name,
        "experience_years": profile.experience_years,
        "skills": [
            skill.name
            for skill in profile.skills
        ],
        "preference": (
            {
                "id": profile.preference.id,
                "desired_position": profile.preference.desired_position,
                "desired_location": profile.preference.desired_location,
                "remote": profile.preference.remote,
                "min_salary": profile.preference.min_salary,
            }
            if profile.preference
            else None
        ),
    }


@router.put("")
def update_profile(
    data: ProfileCreate,
    db: Annotated[Session, Depends(get_db)],
    user: Annotated[User, Depends(get_current_user)],
):
    profile = create_or_update_profile(
        db=db,
        user=user,
        name=data.name,
        experience_years=data.experience_years,
        languages=[],
        education=[],
        desired_positions=[],
        skills=[],
    )

    if data.preference is not None:
        create_or_update_preferences(
            db=db,
            profile_id=profile.id,
            desired_position=data.preference.desired_position,
            desired_location=data.preference.desired_location,
            remote=data.preference.remote,
            min_salary=data.preference.min_salary,
        )

    return read_profile(
        db=db,
        user=user,
    )


@router.put("/preferences")
def update_preferences(
    data: PreferenceCreate,
    db: Annotated[Session, Depends(get_db)],
    user: Annotated[User, Depends(get_current_user)],
):
    profile = get_profile(db, user.id)

    if profile is None:
        raise HTTPException(
            status_code=404,
            detail="Profile not found",
        )

    return create_or_update_preferences(
        db=db,
        profile_id=profile.id,
        desired_position=data.desired_position,
        desired_location=data.desired_location,
        remote=data.remote,
        min_salary=data.min_salary,
    )