"""remove created_at from users"""

from typing import Sequence, Union

from alembic import op


revision: str = "28472096d319"
down_revision: Union[str, Sequence[str], None] = "525cb0ad51d0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column("users", "created_at")


def downgrade() -> None:
    raise NotImplementedError