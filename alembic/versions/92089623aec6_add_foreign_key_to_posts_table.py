"""add foreign-key to posts table

Revision ID: 92089623aec6
Revises: 071116a47838
Create Date: 2021-11-21 23:38:53.246930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92089623aec6'
down_revision = '071116a47838'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'posts',
        sa.Column('owner_id', sa.Integer(), nullable=False)
    )
    op.create_foreign_key(
        'post_users_fk',
        source_table="posts",
        referent_table="users",
        local_cols=['owner_id'],
        remote_cols=['id'],
        ondelete="CASCADE"
    )
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
