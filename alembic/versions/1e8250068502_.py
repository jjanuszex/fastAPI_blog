"""empty message

Revision ID: 1e8250068502
Revises: 6597ba55ae15
Create Date: 2024-04-01 21:08:45.574762

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1e8250068502'
down_revision: Union[str, None] = '6597ba55ae15'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
