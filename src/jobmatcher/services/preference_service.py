from sqlalchemy.orm import Session

from jobmatcher.models.preference import Preference


def create_or_update_preferences(
    db: Session,
    profile_id: int,
    desired_position: str | None = None,
    desired_location: str | None = None,
    remote: bool = False,
    min_salary: float | None = None,
) -> Preference:

    preference = (
        db.query(Preference)
        .filter(
            Preference.profile_id == profile_id
        )
        .first()
    )

    if preference is None:
        preference = Preference(
            profile_id=profile_id,
            desired_position=desired_position,
            desired_location=desired_location,
            remote=remote,
            min_salary=min_salary,
        )

        db.add(preference)

    else:
        preference.desired_position = desired_position
        preference.desired_location = desired_location
        preference.remote = remote
        preference.min_salary = min_salary

    db.commit()
    db.refresh(preference)

    return preference