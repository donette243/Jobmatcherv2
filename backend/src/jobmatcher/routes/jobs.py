from fastapi import APIRouter, HTTPException

from jobmatcher.database.database import SessionLocal
from jobmatcher.models.job import Job
from jobmatcher.services.recommendation_service import (
    get_recommendations,
)

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"],
)


@router.get("")
def get_jobs():
    db = SessionLocal()

    try:
        jobs = db.query(Job).all()

        return [
            {
                "id": job.id,
                "title": job.title,
                "company": job.company,
                "location": job.location,
                "description": job.description,
                "salary_min": job.salary_min,
                "salary_max": job.salary_max,
                "remote": job.remote,
                "url": job.url,
                "published_at": job.published_at,
                "skills": [
                    skill.name
                    for skill in job.skills
                ],
            }
            for job in jobs
        ]

    finally:
        db.close()


@router.get("/recommendations")
def recommendations(profile_id: int):
    db = SessionLocal()

    try:
        return get_recommendations(
            db=db,
            profile_id=profile_id,
        )

    finally:
        db.close()


@router.get("/{job_id}")
def get_job(job_id: int):
    db = SessionLocal()

    try:
        job = (
            db.query(Job)
            .filter(Job.id == job_id)
            .first()
        )

        if job is None:
            raise HTTPException(
                status_code=404,
                detail="Вакансия не найдена.",
            )

        return {
            "id": job.id,
            "title": job.title,
            "company": job.company,
            "location": job.location,
            "description": job.description,
            "salary_min": job.salary_min,
            "salary_max": job.salary_max,
            "remote": job.remote,
            "url": job.url,
            "published_at": job.published_at,
            "skills": [
                skill.name
                for skill in job.skills
            ],
        }

    finally:
        db.close()