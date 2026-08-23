from sqlalchemy.orm import Session

from jobmatcher.models.job import Job
from jobmatcher.schemas.job import JobData


def save_job(
    db: Session,
    job_data: JobData,
) -> Job:

    existing_job = None

    if job_data.external_id:
        existing_job = (
            db.query(Job)
            .filter(
                Job.external_id == job_data.external_id,
                Job.source == job_data.source,
            )
            .first()
        )

    if existing_job:
        return existing_job

    job = Job(
        external_id=job_data.external_id,
        title=job_data.title,
        company=job_data.company,
        description=job_data.description,
        location=job_data.location,
        salary_min=job_data.salary_min,
        salary_max=job_data.salary_max,
        remote=job_data.remote,
        source=job_data.source,
        url=job_data.url,
        published_at=job_data.published_at,
    )

    db.add(job)
    db.commit()
    db.refresh(job)

    return job

def save_jobs(
    db: Session,
    jobs: list[JobData],
) -> int:

    saved_count = 0

    for job_data in jobs:

        existing_job = None

        if job_data.external_id:
            existing_job = (
                db.query(Job)
                .filter(
                    Job.external_id == job_data.external_id,
                    Job.source == job_data.source,
                )
                .first()
            )

        if existing_job:
            continue

        job = Job(
            external_id=job_data.external_id,
            title=job_data.title,
            company=job_data.company,
            description=job_data.description,
            location=job_data.location,
            salary_min=job_data.salary_min,
            salary_max=job_data.salary_max,
            remote=job_data.remote,
            source=job_data.source,
            url=job_data.url,
            published_at=job_data.published_at,
        )

        db.add(job)

        saved_count += 1

    db.commit()

    return saved_count
