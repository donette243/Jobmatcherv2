from sqlalchemy.orm import Session

from jobmatcher.models.job import Job
from jobmatcher.models.profile import Profile
from jobmatcher.services.matching_service import (
    calculate_match_score,
)


def get_recommendations(
    db: Session,
    profile_id: int,
):
    profile = (
        db.query(Profile)
        .filter(Profile.id == profile_id)
        .first()
    )

    if not profile:
        return []

    jobs = db.query(Job).all()

    recommendations = []

    for job in jobs:
        final_score = calculate_match_score(
            profile,
            job,
        )

        recommendations.append(
            {
                "job_id": job.id,
                "title": job.title,
                "company": job.company,
                "location": job.location,
                "description": job.description,
                "salary_min": job.salary_min,
                "salary_max": job.salary_max,
                "remote": job.remote,
                "score": final_score,
                "url": job.url,
                "skills": [
                    skill.name
                    for skill in job.skills
                ],
            }
        )

    recommendations.sort(
        key=lambda item: item["score"],
        reverse=True,
    )

    return recommendations