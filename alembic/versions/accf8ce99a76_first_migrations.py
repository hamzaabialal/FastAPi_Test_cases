"""first migrations

Revision ID: accf8ce99a76
Revises: 779a383512dc
Create Date: 2024-01-19 14:38:23.867761

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'accf8ce99a76'
down_revision: Union[str, None] = '779a383512dc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
