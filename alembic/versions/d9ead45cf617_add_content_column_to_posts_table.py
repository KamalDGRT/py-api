"""add content column to posts table

Revision ID: d9ead45cf617
Revises: b6cbd9746aef
Create Date: 2021-11-21 23:23:29.755277

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9ead45cf617'
down_revision = 'b6cbd9746aef'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'posts',
        sa.Column('content', sa.String(), nullable=False)
    )
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
