"""add users table

Revision ID: 071116a47838
Revises: d9ead45cf617
Create Date: 2021-11-21 23:31:08.893768

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '071116a47838'
down_revision = 'd9ead45cf617'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column(
            'created_at',
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text('now()'),
            nullable=False
        ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    pass


def downgrade():
    op.drop_table('users')
    pass
