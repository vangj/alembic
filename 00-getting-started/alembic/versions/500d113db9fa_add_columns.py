"""add columns

Revision ID: 500d113db9fa
Revises: 30c4eb180be1
Create Date: 2021-06-03 17:00:59.373850

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '500d113db9fa'
down_revision = '30c4eb180be1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'user',
        sa.Column('first_name', sa.String)
    )
    op.add_column(
        'user',
        sa.Column('last_name', sa.String)
    )


def downgrade():
    op.drop_column('user', 'first_name')
    op.drop_column('user', 'last_name')
