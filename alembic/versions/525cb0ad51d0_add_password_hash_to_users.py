"""add password hash to users

Revision ID: 525cb0ad51d0
Revises: 555da135dce7
Create Date: 2026-08-20

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "525cb0ad51d0"
down_revision: Union[str, Sequence[str], None] = "555da135dce7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column(
            "password_hash",
            sa.String(length=255),
            nullable=True,
        ),
    )

    op.execute(
        "UPDATE users SET password_hash = 'TEMPORARY_PASSWORD_HASH'"
    )

    op.alter_column(
        "users",
        "password_hash",
        existing_type=sa.String(length=255),
        nullable=False,
    )


def downgrade() -> None:
    op.drop_column("users", "password_hash")