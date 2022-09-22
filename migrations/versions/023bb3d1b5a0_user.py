"""user

Revision ID: 023bb3d1b5a0
Revises: 
Create Date: 2022-09-09 23:43:06.807636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '023bb3d1b5a0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.TEXT(), nullable=False),
    sa.Column('password', sa.TEXT(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###