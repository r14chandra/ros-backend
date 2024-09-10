"""add created_at field to rh_accounts

Revision ID: 52381cafc36f
Revises: 020def9f5b94
Create Date: 2024-08-28 16:11:42.517790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52381cafc36f'
down_revision = '020def9f5b94'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('rh_accounts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))
        batch_op.create_index(
            'ix_rh_accounts_created_at', ['created_at'],
            unique=False, postgresql_using='brin'
        )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('rh_accounts', schema=None) as batch_op:
        batch_op.drop_index('ix_rh_accounts_created_at')
        batch_op.drop_column('created_at')
    # ### end Alembic commands ###
