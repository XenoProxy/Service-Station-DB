"""nullable

Revision ID: eec41ca03fd8
Revises: e8e32f863e0c
Create Date: 2021-07-24 22:56:01.312663

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'eec41ca03fd8'
down_revision = 'e8e32f863e0c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('auto', sa.Column('owner', sa.Integer(), nullable=True))
    op.alter_column('auto', 'number',
               existing_type=mysql.VARCHAR(length=15),
               nullable=False)
    op.create_foreign_key(None, 'auto', 'clients', ['owner'], ['id'])
    op.alter_column('clients', 'name',
               existing_type=mysql.VARCHAR(length=15),
               nullable=False)
    op.alter_column('clients', 'surname',
               existing_type=mysql.VARCHAR(length=20),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('clients', 'surname',
               existing_type=mysql.VARCHAR(length=20),
               nullable=True)
    op.alter_column('clients', 'name',
               existing_type=mysql.VARCHAR(length=15),
               nullable=True)
    op.drop_constraint(None, 'auto', type_='foreignkey')
    op.alter_column('auto', 'number',
               existing_type=mysql.VARCHAR(length=15),
               nullable=True)
    op.drop_column('auto', 'owner')
    # ### end Alembic commands ###
