# b3c5602e1a6f_inital_blyat.py

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b3c5602e1a6f'
down_revision = 'ac5f3bbae7d6'
branch_labels = None
depends_on = None

def upgrade():
    # op.create_table(
    #     'soundkits',
    #     sa.Column('id', sa.Integer(), primary_key=True),
    #     sa.Column('name', sa.String, nullable=False),
    #     sa.Column('description', sa.String, nullable=True),
    #     sa.Column('picture_url', sa.String, nullable=True),
    #     sa.Column('file_url', sa.String, nullable=False),
    #     sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False),
    #     sa.Column('is_available', sa.Boolean(), nullable=False),
    #     sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    #     sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    # )

    # op.create_table(
    #     'user_to_soundkits_association_table',
    #     sa.Column('soundkit_id', sa.Integer, sa.ForeignKey('soundkits.id'), primary_key=True),
    #     sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), primary_key=True)
    # )

    op.create_table(
        'view',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('beats_id', sa.Integer, sa.ForeignKey('beats.id'), index=True),
        sa.Column('soundkits_id', sa.Integer, sa.ForeignKey('soundkits.id'), index=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), index=True, nullable=True),
        sa.Column('timestamp', sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column('is_available', sa.Boolean(), nullable=False),
        sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    )
        

def downgrade():
    # op.drop_table('user_to_soundkits_association_table')
    # op.drop_table('soundkits')
    op.drop_table('view')
