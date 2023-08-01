"""revision 3

Revision ID: 80278cab1284
Revises: 1e5b14a7a7a7
Create Date: 2023-08-01 18:32:17.765428

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80278cab1284'
down_revision = '1e5b14a7a7a7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('product_full_image', sa.String(length=256), nullable=False))
    op.add_column('products', sa.Column('product_thumbnail', sa.String(length=256), nullable=False))
    op.drop_column('products', 'product_image')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('product_image', sa.VARCHAR(length=256), autoincrement=False, nullable=False))
    op.drop_column('products', 'product_thumbnail')
    op.drop_column('products', 'product_full_image')
    # ### end Alembic commands ###