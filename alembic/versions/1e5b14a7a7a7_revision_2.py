"""revision 2

Revision ID: 1e5b14a7a7a7
Revises: 5a9bba132df1
Create Date: 2023-08-01 14:13:29.930151

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e5b14a7a7a7'
down_revision = '5a9bba132df1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('public_id', sa.String(length=256), nullable=False),
    sa.Column('product_name', sa.String(length=256), nullable=False),
    sa.Column('product_description', sa.String(length=256), nullable=False),
    sa.Column('unit_price', sa.Integer(), nullable=False),
    sa.Column('ranking', sa.Integer(), nullable=False),
    sa.Column('product_image', sa.String(length=256), nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_index(op.f('ix_products_id'), 'products', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_products_id'), table_name='products')
    op.drop_table('products')
    # ### end Alembic commands ###
