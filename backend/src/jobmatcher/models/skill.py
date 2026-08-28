from typing import TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from jobmatcher.database.database import Base

if TYPE_CHECKING:
    from jobmatcher.models.profile import Profile
    from jobmatcher.models.job import Job


class Skill(Base):
    __tablename__ = "skills"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        index=True,
        nullable=False,
    )

    profiles: Mapped[list["Profile"]] = relationship(
        "Profile",
        secondary="profile_skills",
        back_populates="skills",
    )

    jobs: Mapped[list["Job"]] = relationship(
        "Job",
        secondary="job_skills",
        back_populates="skills",
    )