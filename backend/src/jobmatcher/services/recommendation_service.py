from sqlalchemy.orm import Session
from jobmatcher.models.job import Job
from jobmatcher.models.profile import Profile
from jobmatcher.services.matching_service import (
    # calculate_salary_score,
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

    profile_skills = [
        skill.name
        for skill in profile.skills
    ]

    jobs = db.query(Job).all()

    recommendations = []

    for job in jobs:

        job_skills = [
            skill.name
            for skill in job.skills
        ]

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
                "score": final_score,
                "url": job.url,
            }
        )

    recommendations.sort(
        key=lambda item: item["score"],
        reverse=True,
    )

    return recommendations
