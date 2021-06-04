"""create user table

Revision ID: 30c4eb180be1
Revises: 
Create Date: 2021-06-03 16:56:09.944053

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30c4eb180be1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
        sa.Column('email', sa.String, nullable=False),
        sa.Column('password', sa.String, nullable=False)
    )


def downgrade():
    op.drop_table('user')
