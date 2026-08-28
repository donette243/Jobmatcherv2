from typing import TYPE_CHECKING
from sqlalchemy import Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from jobmatcher.database.database import Base

if TYPE_CHECKING:
    from jobmatcher.models.preference import Preference
    from jobmatcher.models.skill import Skill
    from jobmatcher.models.user import User


class Profile(Base):
    __tablename__ = "profiles"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        unique=True,
    )

    name: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    experience_years: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="profile",
    )

    skills: Mapped[list["Skill"]] = relationship(
        "Skill",
        secondary="profile_skills",
        back_populates="profiles",
    )

    preference: Mapped["Preference | None"] = relationship(
        "Preference",
        back_populates="profile",
        uselist=False,
        cascade="all, delete-orphan",
    )