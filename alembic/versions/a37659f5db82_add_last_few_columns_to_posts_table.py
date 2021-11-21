"""add last few columns to posts table

Revision ID: a37659f5db82
Revises: 92089623aec6
Create Date: 2021-11-21 23:43:20.278963

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a37659f5db82'
down_revision = '92089623aec6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'posts',
        sa.Column(
            'published',
            sa.Boolean(),
            nullable=False,
            server_default='TRUE'
        ),
    )
    op.add_column(
        'posts',
        sa.Column(
            'created_at',
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text('NOW()')
        ),
    )
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
