"""empty message

Revision ID: f51396b1461d
Revises: c83be6f21755
Create Date: 2017-05-10 11:22:37.169000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f51396b1461d'
down_revision = 'c83be6f21755'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cms_role', sa.Column('permissions', sa.Integer(), nullable=False))
    op.drop_column('cms_role', 'permission')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cms_role', sa.Column('permission', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.drop_column('cms_role', 'permissions')
    # ### end Alembic commands ###