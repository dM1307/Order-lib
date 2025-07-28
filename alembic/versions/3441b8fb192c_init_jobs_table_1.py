"""init jobs table 1

Revision ID: 3441b8fb192c
Revises: 13b29014e227
Create Date: 2025-06-08 20:05:26.626807

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3441b8fb192c'
down_revision: Union[str, None] = '13b29014e227'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'jobs',
        sa.Column('id', sa.String(length=36), primary_key=True),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('schedule', sa.String(length=255), nullable=False),
        sa.Column('retries', sa.Integer, nullable=False, default=0),
        sa.Column('priority', sa.Integer, nullable=False, default=0),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.func.now(), onupdate=sa.func.now()),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('jobs')
