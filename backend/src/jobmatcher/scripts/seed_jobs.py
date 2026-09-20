from datetime import datetime

from jobmatcher.database.database import SessionLocal
from jobmatcher.models.job import Job
from jobmatcher.models.skill import Skill


JOBS = [
    {
        "external_id": "demo-001",
        "source": "demo",
        "title": "Junior Python Backend Developer",
        "company": "TechNova",
        "location": "Москва",
        "description": "Разработка REST API и backend-сервисов на Python и FastAPI.",
        "salary_min": 90000,
        "salary_max": 140000,
        "remote": False,
        "skills": ["Python", "FastAPI", "SQL", "Git"],
    },
    {
        "external_id": "demo-002",
        "source": "demo",
        "title": "Python Backend Developer",
        "company": "Digital Solutions",
        "location": "Москва",
        "description": "Разработка backend-сервисов и REST API на Python.",
        "salary_min": 130000,
        "salary_max": 190000,
        "remote": True,
        "skills": ["Python", "FastAPI", "SQL", "MySQL", "Docker"],
    },
    {
        "external_id": "demo-003",
        "source": "demo",
        "title": "FastAPI Developer",
        "company": "CloudTech",
        "location": "Санкт-Петербург",
        "description": "Разработка API на FastAPI, SQLAlchemy и MySQL.",
        "salary_min": 120000,
        "salary_max": 180000,
        "remote": True,
        "skills": ["Python", "FastAPI", "SQLAlchemy", "MySQL", "Docker"],
    },
    {
        "external_id": "demo-004",
        "source": "demo",
        "title": "Django Backend Developer",
        "company": "WebSystems",
        "location": "Москва",
        "description": "Разработка веб-сервисов на Python и Django.",
        "salary_min": 120000,
        "salary_max": 180000,
        "remote": False,
        "skills": ["Python", "Django", "PostgreSQL", "Git"],
    },
    {
        "external_id": "demo-005",
        "source": "demo",
        "title": "Java Backend Developer",
        "company": "Enterprise Lab",
        "location": "Санкт-Петербург",
        "description": "Разработка серверных приложений на Java и Spring Boot.",
        "salary_min": 140000,
        "salary_max": 210000,
        "remote": False,
        "skills": ["Java", "Spring Boot", "PostgreSQL", "Docker"],
    },
    {
        "external_id": "demo-006",
        "source": "demo",
        "title": "Junior Java Developer",
        "company": "SoftLine Demo",
        "location": "Казань",
        "description": "Разработка и поддержка Java-приложений.",
        "salary_min": 80000,
        "salary_max": 130000,
        "remote": True,
        "skills": ["Java", "Spring Boot", "SQL", "Git"],
    },
    {
        "external_id": "demo-007",
        "source": "demo",
        "title": "Frontend React Developer",
        "company": "WebStudio",
        "location": "Москва",
        "description": "Разработка пользовательских интерфейсов на React.",
        "salary_min": 110000,
        "salary_max": 180000,
        "remote": True,
        "skills": ["JavaScript", "React", "HTML", "CSS", "Git"],
    },
    {
        "external_id": "demo-008",
        "source": "demo",
        "title": "Junior Frontend Developer",
        "company": "Creative Apps",
        "location": "Москва",
        "description": "Разработка интерфейсов веб-приложений.",
        "salary_min": 70000,
        "salary_max": 120000,
        "remote": False,
        "skills": ["JavaScript", "HTML", "CSS", "React"],
    },
    {
        "external_id": "demo-009",
        "source": "demo",
        "title": "Full Stack Developer",
        "company": "NextWeb",
        "location": "Москва",
        "description": "Разработка frontend и backend частей веб-приложений.",
        "salary_min": 140000,
        "salary_max": 210000,
        "remote": True,
        "skills": ["Python", "FastAPI", "React", "JavaScript", "SQL"],
    },
    {
        "external_id": "demo-010",
        "source": "demo",
        "title": "Data Analyst",
        "company": "DataLab",
        "location": "Москва",
        "description": "Анализ данных и подготовка аналитических отчетов.",
        "salary_min": 100000,
        "salary_max": 160000,
        "remote": True,
        "skills": ["Python", "SQL", "Pandas", "Excel"],
    },
    {
        "external_id": "demo-011",
        "source": "demo",
        "title": "Junior Data Analyst",
        "company": "Analytics Group",
        "location": "Казань",
        "description": "Работа с данными, SQL-запросами и отчетами.",
        "salary_min": 70000,
        "salary_max": 110000,
        "remote": False,
        "skills": ["SQL", "Python", "Excel", "Pandas"],
    },
    {
        "external_id": "demo-012",
        "source": "demo",
        "title": "Data Engineer",
        "company": "BigData Systems",
        "location": "Москва",
        "description": "Разработка процессов обработки и хранения данных.",
        "salary_min": 150000,
        "salary_max": 230000,
        "remote": True,
        "skills": ["Python", "SQL", "PostgreSQL", "Docker"],
    },
    {
        "external_id": "demo-013",
        "source": "demo",
        "title": "Machine Learning Engineer",
        "company": "AI Research Lab",
        "location": "Москва",
        "description": "Разработка и внедрение моделей машинного обучения.",
        "salary_min": 160000,
        "salary_max": 250000,
        "remote": True,
        "skills": ["Python", "PyTorch", "Machine Learning", "Pandas"],
    },
    {
        "external_id": "demo-014",
        "source": "demo",
        "title": "Junior ML Engineer",
        "company": "Smart AI",
        "location": "Санкт-Петербург",
        "description": "Подготовка данных и обучение ML-моделей.",
        "salary_min": 100000,
        "salary_max": 150000,
        "remote": False,
        "skills": ["Python", "Machine Learning", "Pandas", "NumPy"],
    },
    {
        "external_id": "demo-015",
        "source": "demo",
        "title": "DevOps Engineer",
        "company": "Cloud Platform",
        "location": "Москва",
        "description": "Автоматизация развертывания и сопровождение сервисов.",
        "salary_min": 160000,
        "salary_max": 240000,
        "remote": True,
        "skills": ["Docker", "Linux", "Git", "CI/CD"],
    },
    {
        "external_id": "demo-016",
        "source": "demo",
        "title": "QA Automation Engineer",
        "company": "QualitySoft",
        "location": "Москва",
        "description": "Разработка автоматизированных тестов для веб-сервисов.",
        "salary_min": 110000,
        "salary_max": 170000,
        "remote": True,
        "skills": ["Python", "Pytest", "API Testing", "Git"],
    },
    {
        "external_id": "demo-017",
        "source": "demo",
        "title": "Backend API Developer",
        "company": "FinTech Demo",
        "location": "Москва",
        "description": "Разработка REST API и интеграций для backend-систем.",
        "salary_min": 130000,
        "salary_max": 200000,
        "remote": False,
        "skills": ["Python", "FastAPI", "REST API", "SQL", "Docker"],
    },
    {
        "external_id": "demo-018",
        "source": "demo",
        "title": "Python Developer Intern",
        "company": "StartUp Hub",
        "location": "Москва",
        "description": "Стажировка в команде разработки Python-приложений.",
        "salary_min": 50000,
        "salary_max": 80000,
        "remote": True,
        "skills": ["Python", "Git", "SQL"],
    },
    {
        "external_id": "demo-019",
        "source": "demo",
        "title": "Database Developer",
        "company": "DataCore",
        "location": "Санкт-Петербург",
        "description": "Разработка и оптимизация SQL-запросов и баз данных.",
        "salary_min": 110000,
        "salary_max": 170000,
        "remote": False,
        "skills": ["SQL", "MySQL", "PostgreSQL", "Python"],
    },
    {
        "external_id": "demo-020",
        "source": "demo",
        "title": "Software Engineer",
        "company": "Innovation Systems",
        "location": "Москва",
        "description": "Разработка и поддержка современных программных систем.",
        "salary_min": 130000,
        "salary_max": 200000,
        "remote": True,
        "skills": ["Python", "Git", "Docker", "SQL", "REST API"],
    },
]


def get_or_create_skill(db, name: str) -> Skill:
    skill = db.query(Skill).filter(Skill.name == name).first()

    if skill is None:
        skill = Skill(name=name)
        db.add(skill)
        db.flush()

    return skill


def seed_jobs() -> None:
    db = SessionLocal()

    try:
        added = 0
        skipped = 0

        for data in JOBS:
            existing_job = (
                db.query(Job)
                .filter(Job.external_id == data["external_id"])
                .first()
            )

            if existing_job is not None:
                skipped += 1
                continue

            skills = [
                get_or_create_skill(db, skill_name)
                for skill_name in data["skills"]
            ]

            job = Job(
                external_id=data["external_id"],
                source=data["source"],
                title=data["title"],
                company=data["company"],
                location=data["location"],
                description=data["description"],
                salary_min=data["salary_min"],
                salary_max=data["salary_max"],
                remote=data["remote"],
                url=None,
                published_at=datetime.now(),
                skills=skills,
            )

            db.add(job)
            added += 1

        db.commit()

        print(f"Demo jobs added: {added}. Already existed: {skipped}.")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_jobs()
