"""empty message

Revision ID: 8205a111aef5
Revises: 4f5ad222237f
Create Date: 2017-06-05 11:41:24.473000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8205a111aef5'
down_revision = '4f5ad222237f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('highlight_post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'post', sa.Column('highlight_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'post', 'highlight_post', ['highlight_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.drop_column(u'post', 'highlight_id')
    op.drop_table('highlight_post')
    # ### end Alembic commands ###