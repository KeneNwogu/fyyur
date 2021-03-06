"""empty message

Revision ID: e75f9b4fdfee
Revises: 31cfb0e6d36d
Create Date: 2022-05-28 14:11:24.888820

"""
from datetime import datetime

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e75f9b4fdfee'
down_revision = '31cfb0e6d36d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Show', sa.Column('start_date', sa.DateTime(), nullable=False, server_default=str(datetime.utcnow())))
    op.drop_column('Show', 'start_time')
    op.drop_column('Venue', 'genres')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('genres', postgresql.ARRAY(sa.VARCHAR(length=50)), autoincrement=False, nullable=True))
    op.add_column('Show', sa.Column('start_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('Show', 'start_date')
    # ### end Alembic commands ###
