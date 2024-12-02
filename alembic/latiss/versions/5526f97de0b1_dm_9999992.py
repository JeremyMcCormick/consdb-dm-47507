"""DM-9999992

Revision ID: 5526f97de0b1
Revises: 47c0b5ce839e
Create Date: 2024-12-02 23:12:26.214035+00:00

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = "5526f97de0b1"
down_revision: Union[str, None] = "47c0b5ce839e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "ccdvisit1_quicklook",
        sa.Column(
            "dummy_col1",
            sa.INTEGER().with_variant(mysql.INTEGER(), "mysql").with_variant(sa.INTEGER(), "postgresql"),
            nullable=True,
            comment="Dummy column 1",
        ),
        schema="cdb_latiss",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("ccdvisit1_quicklook", "dummy_col1", schema="cdb_latiss")
    # ### end Alembic commands ###
