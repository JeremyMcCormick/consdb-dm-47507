"""fix vignetting

Revision ID: 3f8460378c1e
Revises: ef3efe082be3
Create Date: 2024-06-25 21:29:01.650070+00:00

"""

from typing import Sequence, Union

import sqlalchemy as sa
from sqlalchemy.dialects import mysql, oracle

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "3f8460378c1e"
down_revision: Union[str, None] = "ef3efe082be3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "exposure",
        "vignette",
        existing_type=sa.INTEGER(),
        type_=sa.VARCHAR(length=10)
        .with_variant(mysql.VARCHAR(length=10), "mysql")
        .with_variant(oracle.VARCHAR2(length=10), "oracle")
        .with_variant(sa.VARCHAR(length=10), "postgresql"),
        comment="Instrument blocked from the sky: UNKNOWN, NO, PARTIALLY, FULLY.",
        existing_comment="Instrument blocked from the sky: Unknown = 0, No = 1, Partially = 2, Fully = 3.",
        existing_nullable=True,
        schema="cdb_lsstcomcamsim",
    )
    op.alter_column(
        "exposure",
        "vignette_min",
        existing_type=sa.INTEGER(),
        type_=sa.VARCHAR(length=10)
        .with_variant(mysql.VARCHAR(length=10), "mysql")
        .with_variant(oracle.VARCHAR2(length=10), "oracle")
        .with_variant(sa.VARCHAR(length=10), "postgresql"),
        comment="Lowest amount of instrument vignetting detected during the exposure: UNKNOWN, NO, PARTIALLY, FULLY.",
        existing_comment="Minimum value of vignette during the exposure.",
        existing_nullable=True,
        schema="cdb_lsstcomcamsim",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "exposure",
        "vignette_min",
        existing_type=sa.VARCHAR(length=10)
        .with_variant(mysql.VARCHAR(length=10), "mysql")
        .with_variant(oracle.VARCHAR2(length=10), "oracle")
        .with_variant(sa.VARCHAR(length=10), "postgresql"),
        type_=sa.INTEGER(),
        comment="Minimum value of vignette during the exposure.",
        existing_comment="Lowest amount of instrument vignetting detected during the exposure: UNKNOWN, NO, PARTIALLY, FULLY.",
        existing_nullable=True,
        schema="cdb_lsstcomcamsim",
    )
    op.alter_column(
        "exposure",
        "vignette",
        existing_type=sa.VARCHAR(length=10)
        .with_variant(mysql.VARCHAR(length=10), "mysql")
        .with_variant(oracle.VARCHAR2(length=10), "oracle")
        .with_variant(sa.VARCHAR(length=10), "postgresql"),
        type_=sa.INTEGER(),
        comment="Instrument blocked from the sky: Unknown = 0, No = 1, Partially = 2, Fully = 3.",
        existing_comment="Instrument blocked from the sky: UNKNOWN, NO, PARTIALLY, FULLY.",
        existing_nullable=True,
        schema="cdb_lsstcomcamsim",
    )
    # ### end Alembic commands ###
