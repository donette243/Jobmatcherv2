from app.database.database import SessionLocal
from app.models.job import Job
from app.services.job_skill_service import (
    attach_skills_to_job,
)


db = SessionLocal()

try:

    jobs = db.query(Job).all()

    for job in jobs:

        skills = attach_skills_to_job(
            db,
            job,
        )

        print(
            f"{job.title}: "
            f"{[skill.name for skill in skills]}"
        )

finally:
    db.close()