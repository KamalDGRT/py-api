"""create posts table

Revision ID: b6cbd9746aef
Revises: 
Create Date: 2021-11-21 23:13:10.683344

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6cbd9746aef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('title', sa.String(), nullable=False)
    )
    pass


def downgrade():
    op.drop_table('posts')
    pass
