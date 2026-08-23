from sqlalchemy import select
from sqlalchemy.orm import Session

from jobmatcher.models.job import Job
from jobmatcher.models.skill import Skill


def get_or_create_skill(
    db: Session,
    name: str,
) -> Skill:

    normalized = name.strip().lower()

    statement = select(Skill).where(
        Skill.name == normalized
    )

    skill = db.scalar(statement)

    if skill is not None:
        return skill

    skill = Skill(
        name=normalized
    )

    db.add(skill)
    db.flush()

    return skill


def attach_skills_to_job(
    db: Session,
    job: Job,
    skills: list[str],
) -> Job:

    job.skills.clear()

    for skill_name in skills:

        if not skill_name.strip():
            continue

        skill = get_or_create_skill(
            db,
            skill_name,
        )

        if skill not in job.skills:
            job.skills.append(skill)

    db.commit()
    db.refresh(job)

    return job