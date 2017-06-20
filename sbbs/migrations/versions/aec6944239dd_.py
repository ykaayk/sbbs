"""empty message

Revision ID: aec6944239dd
Revises: fef0318c5982
Create Date: 2017-06-19 16:53:59.227000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aec6944239dd'
down_revision = 'fef0318c5982'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('front_user', sa.Column('old_login_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('front_user', 'old_login_time')
    # ### end Alembic commands ###