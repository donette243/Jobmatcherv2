from typing import Any
import requests
from jobmatcher.schemas.job import JobData
class JobCollector:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def fetch(self, params: dict[str, Any] | None = None):
        response = requests.get(
            self.base_url,
            params=params,
            timeout=20,
        )

        response.raise_for_status()

        return response.json()

    def parse_jobs(
        self,
        data: dict[str, Any],
    ) -> list[JobData]:

        jobs = []

        for item in data.get("items", []):

            job = JobData(
                external_id=str(item.get("id"))
                if item.get("id") is not None
                else None,

                title=item.get("title", ""),

                company=item.get("company"),

                description=item.get("description"),

                location=item.get("location"),

                salary_min=item.get("salary_min"),

                salary_max=item.get("salary_max"),

                remote=bool(item.get("remote", False)),

                source="api",

                url=item.get("url"),

                published_at=None,
            )

            jobs.append(job)

        return jobs
