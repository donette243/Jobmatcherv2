from fastapi import APIRouter
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
                "salary_min": job.salary_min,
                "salary_max": job.salary_max,
                "remote": job.remote,
                "url": job.url,
            }
            for job in jobs
        ]

    finally:
        db.close()
@router.get("/recommendations")
def recommendations(
    profile_id: int,
):

    db = SessionLocal()

    try:

        return get_recommendations(
            db=db,
            profile_id=profile_id,
        )

    finally:
        db.close()
