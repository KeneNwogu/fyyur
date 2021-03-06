"""empty message

Revision ID: 7372a16b6aa4
Revises: 
Create Date: 2022-05-27 22:22:55.705655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7372a16b6aa4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Show',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.Column('venue_id', sa.Integer(), nullable=True),
    sa.Column('artist_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('Artist', sa.Column('seeking_venues', sa.Boolean(), server_default='true', nullable=False))
    op.add_column('Artist', sa.Column('seeking_description', sa.Text(), nullable=True))
    op.add_column('Venue', sa.Column('seeking_talent', sa.Boolean(), server_default='true', nullable=False))
    op.add_column('Venue', sa.Column('seeking_description', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'seeking_description')
    op.drop_column('Venue', 'seeking_talent')
    op.drop_column('Artist', 'seeking_description')
    op.drop_column('Artist', 'seeking_venues')
    op.drop_table('Show')
    # ### end Alembic commands ###
