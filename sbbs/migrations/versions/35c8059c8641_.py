"""empty message

Revision ID: 35c8059c8641
Revises: b39b2f4a00d0
Create Date: 2017-05-08 11:20:28.525000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35c8059c8641'
down_revision = 'b39b2f4a00d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cms_role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('desc', sa.String(length=100), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('permission', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cms_user_role',
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['cms_role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['cms_user.id'], ),
    sa.PrimaryKeyConstraint('role_id', 'user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cms_user_role')
    op.drop_table('cms_role')
    # ### end Alembic commands ###
