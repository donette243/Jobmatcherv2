from jobmatcher.schemas.job import JobData
from jobmatcher.services.job_service import save_jobs


def test_save_jobs(db):
    jobs = [
        JobData(
            external_id="test-001",
            title="Backend Developer",
            company="Test Company",
            description="Python FastAPI SQL",
            location="Moscow",
            salary_min=150000,
            salary_max=200000,
            remote=True,
            source="test",
            url="https://example.com/job/1",
            published_at=None,
        ),
        JobData(
            external_id="test-002",
            title="Data Analyst",
            company="Test Company",
            description="Python SQL Pandas",
            location="Moscow",
            salary_min=120000,
            salary_max=170000,
            remote=False,
            source="test",
            url="https://example.com/job/2",
            published_at=None,
        ),
    ]

    count = save_jobs(db, jobs)

    assert count == 2