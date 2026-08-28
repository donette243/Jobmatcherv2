from typing import TYPE_CHECKING
from datetime import datetime
from sqlalchemy import DateTime, Float, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from jobmatcher.database.database import Base

if TYPE_CHECKING:
    from jobmatcher.models.skill import Skill


class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    external_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        unique=True,
        index=True,
    )

    source: Mapped[str] = mapped_column(
    String(255),
    nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    company: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    location: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    salary_min: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    salary_max: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    remote: Mapped[bool] = mapped_column(
        default=False,
        nullable=False,
    )

    url: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )

    skills: Mapped[list["Skill"]] = relationship(
        "Skill",
        secondary="job_skills",
        back_populates="jobs",
    )

    published_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )