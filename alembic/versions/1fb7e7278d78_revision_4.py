"""revision 4

Revision ID: 1fb7e7278d78
Revises: 80278cab1284
Create Date: 2023-08-02 10:30:24.579882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fb7e7278d78'
down_revision = '80278cab1284'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('products_public_id_key', 'products', type_='unique')
    op.drop_column('products', 'public_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('public_id', sa.VARCHAR(length=256), autoincrement=False, nullable=False))
    op.create_unique_constraint('products_public_id_key', 'products', ['public_id'])
    # ### end Alembic commands ###
