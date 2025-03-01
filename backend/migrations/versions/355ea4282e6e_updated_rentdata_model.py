"""Updated RentData model

Revision ID: 355ea4282e6e
Revises: c8903837f3c7
Create Date: 2025-02-24 18:15:16.592918

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '355ea4282e6e'
down_revision: Union[str, None] = 'c8903837f3c7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('rent_data', 'neighborhood',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('rent_data', 'rent_price',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('rent_data', 'rent_price',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('rent_data', 'neighborhood',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
