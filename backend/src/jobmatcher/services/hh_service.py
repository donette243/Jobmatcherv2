import requests
from datetime import datetime
from sqlalchemy.orm import Session
from jobmatcher.models.job import Job


HH_API_URL = "https://api.hh.ru/vacancies"

HEADERS = {
    "HH-User-Agent": "JobMatcher/1.0 (Donet; ton-email@gmail.com)",
    "Accept": "application/json",
}

def fetch_hh_jobs(
    db: Session,
    text: str = "Python",
    area: int = 1,
    per_page: int = 20,
):
    params = {
        "text": text,
        "area": area,
        "per_page": per_page,
        "page": 0,
    }

    response = requests.get(
        HH_API_URL,
        params=params,
        headers=HEADERS,
        timeout=15,
    )

    response.raise_for_status()

    data = response.json()

    created_jobs = []

    for item in data.get("items", []):
        external_id = str(item["id"])

        existing_job = (
            db.query(Job)
            .filter(Job.external_id == external_id)
            .first()
        )

        if existing_job:
            continue

        salary = item.get("salary")

        salary_min = None
        salary_max = None

        if salary:
            salary_min = salary.get("from")
            salary_max = salary.get("to")

        employer = item.get("employer") or {}
        area_data = item.get("area") or {}

        published_at = None

        if item.get("published_at"):
            published_at = datetime.fromisoformat(
                item["published_at"].replace("Z", "+00:00")
            )

        job = Job(
            external_id=external_id,
            source="hh.ru",
            title=item.get("name", "Sans titre"),
            company=employer.get("name"),
            location=area_data.get("name"),
            description=None,
            salary_min=salary_min,
            salary_max=salary_max,
            remote=False,
            url=item.get("alternate_url"),
            published_at=published_at,
        )

        db.add(job)
        created_jobs.append(job)

    db.commit()

    return created_jobs