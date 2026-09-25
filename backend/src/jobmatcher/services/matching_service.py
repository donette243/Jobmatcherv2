from jobmatcher.models.job import Job
from jobmatcher.models.profile import Profile


def calculate_skill_match(
    profile: Profile,
    job: Job,
) -> float:
    profile_skills = {
        skill.name.lower().strip()
        for skill in profile.skills
        if skill.name
    }

    job_skills = {
        skill.name.lower().strip()
        for skill in job.skills
        if skill.name
    }

    if not job_skills:
        return 0.0

    if not profile_skills:
        return 0.0

    matched = profile_skills.intersection(
        job_skills
    )

    return (
        len(matched)
        / len(job_skills)
        * 100
    )


def calculate_experience_match(
    profile: Profile,
    job: Job,
) -> float:
    return 100.0


def calculate_location_match(
    profile: Profile,
    job: Job,
) -> float:
    preference = profile.preference

    if preference is None:
        return 100.0

    desired_location = preference.desired_location

    if not desired_location:
        return 100.0

    job_location = job.location or ""

    if not job_location:
        return 0.0

    desired_location = (
        str(desired_location)
        .lower()
        .strip()
    )

    job_location = (
        str(job_location)
        .lower()
        .strip()
    )

    if desired_location in job_location:
        return 100.0

    return 0.0


def calculate_remote_match(
    profile: Profile,
    job: Job,
) -> float:
    preference = profile.preference

    if preference is None:
        return 100.0

    if not preference.remote:
        return 100.0

    return (
        100.0
        if job.remote
        else 0.0
    )


def calculate_match_score(
    profile: Profile,
    job: Job,
) -> float:
    skill_score = calculate_skill_match(
        profile,
        job,
    )

    experience_score = calculate_experience_match(
        profile,
        job,
    )

    location_score = calculate_location_match(
        profile,
        job,
    )

    remote_score = calculate_remote_match(
        profile,
        job,
    )

    score = (
        skill_score * 0.60
        + experience_score * 0.20
        + location_score * 0.10
        + remote_score * 0.10
    )

    return round(
        min(score, 100.0),
        2,
    )


def match_job(
    profile: Profile,
    job: Job,
) -> dict:
    return {
        "job_id": job.id,
        "title": job.title,
        "company": job.company,
        "score": calculate_match_score(
            profile,
            job,
        ),
    }


def match_jobs(
    profile: Profile,
    jobs: list[Job],
) -> list[dict]:
    results = [
        match_job(profile, job)
        for job in jobs
    ]

    return sorted(
        results,
        key=lambda item: item["score"],
        reverse=True,
    )


def calculate_final_score(
    profile: Profile,
    job: Job,
) -> float:
    return calculate_match_score(
        profile,
        job,
    )