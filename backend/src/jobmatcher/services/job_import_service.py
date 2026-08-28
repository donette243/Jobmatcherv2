from sqlalchemy.orm import Session
from jobmatcher.services.job_service import (
    save_job,
)


def import_jobs(
    db: Session,
    jobs: list[dict],
) -> list:

    imported = []

    for job_data in jobs:

        if not job_data.get("title"):
            continue

        job = save_job(
            db,
            job_data,
        )

        imported.append(job)

    return imported