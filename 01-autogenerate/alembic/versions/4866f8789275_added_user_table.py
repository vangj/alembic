"""Added user table

Revision ID: 4866f8789275
Revises: 
Create Date: 2021-06-03 18:52:15.935814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4866f8789275'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('person',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_person_email'), 'person', ['email'], unique=False)
    op.create_index(op.f('ix_person_id'), 'person', ['id'], unique=False)
    op.create_index(op.f('ix_person_password'), 'person', ['password'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_person_password'), table_name='person')
    op.drop_index(op.f('ix_person_id'), table_name='person')
    op.drop_index(op.f('ix_person_email'), table_name='person')
    op.drop_table('person')
    # ### end Alembic commands ###
