"""add calendar and agency into table

Revision ID: 868c59094b3
Revises: 4a003740b70b
Create Date: 2014-12-22 10:29:22.296140

"""

# revision identifiers, used by Alembic.
revision = '868c59094b3'
down_revision = '4a003740b70b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('agency',
    sa.Column('agency_id', sa.String(length=50), nullable=False),
    sa.Column('agency_name', sa.String(length=50), nullable=True),
    sa.Column('agency_url', sa.String(length=50), nullable=True),
    sa.Column('agency_timezone', sa.String(length=50), nullable=True),
    sa.Column('agency_lang', sa.String(length=50), nullable=True),
    sa.Column('agency_phone', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('agency_id')
    )
    op.create_table('calendar',
    sa.Column('service_id', sa.String(length=50), nullable=False),
    sa.Column('start_date', sa.String(length=50), nullable=True),
    sa.Column('end_date', sa.String(length=50), nullable=True),
    sa.Column('monday', sa.String(length=50), nullable=True),
    sa.Column('tuesday', sa.String(length=50), nullable=True),
    sa.Column('wednesday', sa.String(length=50), nullable=True),
    sa.Column('thursday', sa.String(length=50), nullable=True),
    sa.Column('friday', sa.String(length=50), nullable=True),
    sa.Column('saturday', sa.String(length=50), nullable=True),
    sa.Column('sunday', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('service_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('calendar')
    op.drop_table('agency')
    ### end Alembic commands ###