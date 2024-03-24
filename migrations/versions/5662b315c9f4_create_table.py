"""create table

Revision ID: 5662b315c9f4
Revises: 
Create Date: 2024-03-24 17:50:37.742276

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '5662b315c9f4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('urls',
                    sa.Column('key', sa.String(), nullable=False),
                    sa.Column('secret_key', sa.String(), nullable=False),
                    sa.Column('target_url', sa.String(), nullable=False),
                    sa.Column('clicks', sa.Integer(), nullable=False),
                    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
                    sa.Column('id', sa.UUID(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('secret_key')
                    )
    op.create_index(op.f('ix_urls_key'), 'urls', ['key'], unique=True)
    op.create_index(op.f('ix_urls_target_url'), 'urls', ['target_url'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_urls_target_url'), table_name='urls')
    op.drop_index(op.f('ix_urls_key'), table_name='urls')
    op.drop_table('urls')
    # ### end Alembic commands ###