from jobmatcher.schemas.job import JobData
from jobmatcher.schemas.profile import ProfileRead


def _skill_to_string(skill) -> str:
    """
    Convertit une compétence en chaîne de caractères.

    Les compétences peuvent être :
    - directement des strings
    - des objets SQLAlchemy Skill
    - des objets Pydantic contenant un champ name
    - des objets contenant un champ skill
    """
    if isinstance(skill, str):
        return skill

    name = getattr(skill, "name", None)
    if name is not None:
        return str(name)

    value = getattr(skill, "skill", None)
    if value is not None:
        return str(value)

    return str(skill)


def calculate_skill_match(
    profile: ProfileRead,
    job: JobData,
) -> float:
    """
    Calcule le pourcentage de compétences du poste
    présentes dans le profil.
    """

    profile_skills = {
        _skill_to_string(skill).lower().strip()
        for skill in profile.skills
    }

    job_skills = {
        _skill_to_string(skill).lower().strip()
        for skill in job.skills
    }

    # Supprime les valeurs vides
    profile_skills.discard("")
    job_skills.discard("")

    if not job_skills:
        return 0.0

    if not profile_skills:
        return 0.0

    matched = profile_skills.intersection(job_skills)

    return (
        len(matched)
        / len(job_skills)
        * 100
    )


def calculate_experience_match(
    profile: ProfileRead,
    job: JobData,
) -> float:
    """
    Calcule la compatibilité concernant
    les années d'expérience.
    """

    if profile.experience_years is None:
        return 0.0

    required = getattr(
        job,
        "experience_years",
        None,
    )

    # Si le poste ne précise pas d'expérience requise,
    # on considère que le profil correspond.
    if required is None:
        return 100.0

    if required == 0:
        return 100.0

    if profile.experience_years >= required:
        return 100.0

    return min(
        profile.experience_years
        / required
        * 100,
        100.0,
    )


def calculate_location_match(
    profile: ProfileRead,
    job: JobData,
) -> float:
    """
    Calcule la compatibilité entre la localisation
    souhaitée par le profil et celle du poste.
    """

    preference = getattr(
        profile,
        "preference",
        None,
    )

    if preference is None:
        return 100.0

    desired_location = getattr(
        preference,
        "desired_location",
        None,
    )

    if not desired_location:
        return 100.0

    job_location = getattr(
        job,
        "location",
        None,
    ) or ""

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
    profile: ProfileRead,
    job: JobData,
) -> float:
    """
    Calcule la compatibilité concernant le télétravail.
    """

    preference = getattr(
        profile,
        "preference",
        None,
    )

    if preference is None:
        return 100.0

    # Si le profil n'exige pas le télétravail,
    # n'importe quel poste est acceptable.
    if not preference.remote:
        return 100.0

    # Le profil exige le télétravail.
    return (
        100.0
        if getattr(job, "remote", False)
        else 0.0
    )


def calculate_match_score(
    profile: ProfileRead,
    job: JobData,
) -> float:
    """
    Calcule le score global de correspondance.

    Pondération :
    - compétences : 60 %
    - expérience : 20 %
    - localisation : 10 %
    - télétravail : 10 %
    """

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
    profile: ProfileRead,
    job: JobData,
) -> dict:
    """
    Retourne le résultat du matching pour un seul poste.
    """

    return {
        "job_id": job.id,
        "title": job.title,
        "company": getattr(
            job,
            "company",
            None,
        ),
        "score": calculate_match_score(
            profile,
            job,
        ),
    }


def match_jobs(
    profile: ProfileRead,
    jobs: list[JobData],
) -> list[dict]:
    """
    Calcule le score de tous les postes
    puis les trie du meilleur au moins bon.
    """

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
    profile: ProfileRead,
    job: JobData,
) -> float:
    return calculate_match_score(profile, job)