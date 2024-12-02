"""DM-9999992

Revision ID: 15f63fd347d2
Revises: 47c0b5ce839e
Create Date: 2024-12-02 20:12:49.467331+00:00

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = "15f63fd347d2"
down_revision: Union[str, None] = "47c0b5ce839e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "ccdvisit1_quicklook",
        sa.Column(
            "dummy_column1",
            sa.VARCHAR(length=64)
            .with_variant(mysql.VARCHAR(length=64), "mysql")
            .with_variant(sa.VARCHAR(length=64), "postgresql"),
            nullable=True,
            comment="Dummy column for testing.",
        ),
        schema="cdb_latiss",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("ccdvisit1_quicklook", "dummy_column1", schema="cdb_latiss")
    # ### end Alembic commands ###
