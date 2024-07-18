"""create view table

Revision ID: 1d41ae799392
Revises: 8645f6452298
Create Date: 2024-07-18 23:58:39.876325

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1d41ae799392'
down_revision: Union[str, None] = '8645f6452298'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'view',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('beats_id', sa.Integer, sa.ForeignKey('beats.id'), nullable=False),
        sa.Column('soundkits_id', sa.Integer, sa.ForeignKey('soundkits.id'), nullable=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=True),
        sa.Column('is_available', sa.Boolean, default=True),
        sa.Column('timestamp', sa.DateTime(timezone=True), server_default=sa.func.now()),
    )


def downgrade():
    op.drop_table('view')