"""add password reset fields

Revision ID: 84d3dbf61fa8
Revises: 28472096d319
Create Date: 2026-09-02 01:51:15.403410
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "84d3dbf61fa8"
down_revision: Union[str, Sequence[str], None] = "28472096d319"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Add password reset fields to users."""
    op.add_column(
        "users",
        sa.Column(
            "reset_token",
            sa.String(length=255),
            nullable=True,
        ),
    )

    op.add_column(
        "users",
        sa.Column(
            "reset_token_expires_at",
            sa.DateTime(),
            nullable=True,
        ),
    )


def downgrade() -> None:
    """Remove password reset fields from users."""
    op.drop_column(
        "users",
        "reset_token_expires_at",
    )

    op.drop_column(
        "users",
        "reset_token",
    )