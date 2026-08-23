from sqlalchemy.orm import Session

from jobmatcher.models.job import Job
from jobmatcher.models.profile import Profile
from jobmatcher.services.matching_service import (
    # calculate_salary_score,
    calculate_match_score,
    # get_matched_skills,
    # get_missing_skills,
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

        # salary_score = calculate_salary_score(
        #     profile.min_salary,
        #     job.salary_min,
        #     job.salary_max,
        # )

        recommendations.append(
            {
                "job_id": job.id,
                "title": job.title,
                "company": job.company,
                "location": job.location,
                "score": final_score,
                # "matched_skills": get_matched_skills(
                #     profile_skills,
                #     job_skills,
                # ),
                # "missing_skills": get_missing_skills(
                #     profile_skills,
                #     job_skills,
                # ),
                # "skills_score": skills_score,
                # "location_score": location_score,
                # "remote_score": remote_score,
                # "salary_score": salary_score,
                "url": job.url,
            }
        )

    recommendations.sort(
        key=lambda item: item["score"],
        reverse=True,
    )

    return recommendations
