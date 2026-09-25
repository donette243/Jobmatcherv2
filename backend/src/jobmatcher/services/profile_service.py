from sqlalchemy import select
from sqlalchemy.orm import Session

from jobmatcher.models.preference import Preference
from jobmatcher.models.profile import Profile
from jobmatcher.models.skill import Skill
from jobmatcher.models.user import User


def get_profile(
    db: Session,
    user_id: int,
) -> Profile | None:
    statement = select(Profile).where(
        Profile.user_id == user_id
    )

    return db.scalar(statement)


def create_or_update_profile(
    db: Session,
    user: User,
    name: str | None,
    experience_years: float | None,
    languages: list[str],
    education: list[str],
    desired_positions: list[str],
    skills: list[str] | None = None,
) -> Profile:
    profile = get_profile(
        db,
        user.id,
    )

    if profile is None:
        profile = Profile(
            user_id=user.id,
            name=name,
            experience_years=experience_years,
        )

        db.add(profile)

    else:
        profile.name = name
        profile.experience_years = experience_years

    if skills is not None:
        profile.skills.clear()

        normalized_skills = {
            skill.strip().lower()
            for skill in skills
            if skill.strip()
        }

        for skill_name in normalized_skills:
            statement = select(Skill).where(
                Skill.name == skill_name
            )

            skill = db.scalar(statement)

            if skill is None:
                skill = Skill(
                    name=skill_name
                )

                db.add(skill)
                db.flush()

            profile.skills.append(skill)

    db.commit()
    db.refresh(profile)

    return profile


def set_preference(
    db: Session,
    profile: Profile,
    data: dict,
) -> Preference:
    preference = profile.preference

    if preference is None:
        preference = Preference(
            profile_id=profile.id
        )

        db.add(preference)

    fields = (
        "desired_position",
        "desired_location",
        "remote",
        "min_salary",
    )

    for field in fields:
        if field in data:
            setattr(
                preference,
                field,
                data[field],
            )

    db.commit()
    db.refresh(preference)

    return preference