from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from jobmatcher.database.database import Base


class ProfileSkill(Base):
    __tablename__ = "profile_skills"

    profile_id: Mapped[int] = mapped_column(
        ForeignKey("profiles.id", ondelete="CASCADE"),
        primary_key=True,
    )

    skill_id: Mapped[int] = mapped_column(
        ForeignKey("skills.id", ondelete="CASCADE"),
        primary_key=True,
    )