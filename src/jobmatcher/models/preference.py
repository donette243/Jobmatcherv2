from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from jobmatcher.database.database import Base

if TYPE_CHECKING:
    from jobmatcher.models.profile import Profile


class Preference(Base):
    __tablename__ = "preferences"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    profile_id: Mapped[int] = mapped_column(
        ForeignKey("profiles.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
    )

    desired_position: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    desired_location: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    remote: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    min_salary: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    profile: Mapped["Profile"] = relationship(
        "Profile",
        back_populates="preference",
    )