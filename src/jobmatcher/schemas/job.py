from datetime import datetime

from pydantic import BaseModel


class JobData(BaseModel):
    external_id: str | None = None
    title: str
    company: str | None = None
    description: str | None = None
    location: str | None = None
    salary_min: float | None = None
    salary_max: float | None = None
    remote: bool = False
    source: str
    url: str | None = None
    published_at: datetime | None = None
    skills: list[str] = []
    