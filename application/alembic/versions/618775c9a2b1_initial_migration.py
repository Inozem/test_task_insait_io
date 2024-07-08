"""Initial migration

Revision ID: 618775c9a2b1
Revises: 
Create Date: 2024-07-04 16:02:07.257849

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '618775c9a2b1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'question_and_answer',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('question', sa.String(length=4096), nullable=False),
        sa.Column('answer', sa.String(length=4096), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    pass
