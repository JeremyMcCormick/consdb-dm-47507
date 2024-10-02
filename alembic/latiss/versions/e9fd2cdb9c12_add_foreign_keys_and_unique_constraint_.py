"""Add foreign keys and unique constraint for exposure.exposure_id

Revision ID: e9fd2cdb9c12
Revises: 56077b746de8
Create Date: 2024-09-25 21:37:20.956716+00:00

"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "e9fd2cdb9c12"
down_revision: Union[str, None] = "56077b746de8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(
        "un_ccdexposure_exposure_id_detector", "ccdexposure", ["exposure_id", "detector"], schema="cdb_latiss"
    )
    op.create_foreign_key(
        "fk_ccdexposure_exposure_id",
        "ccdexposure",
        "exposure",
        ["exposure_id"],
        ["exposure_id"],
        source_schema="cdb_latiss",
        referent_schema="cdb_latiss",
    )
    op.create_foreign_key(
        "fk_exposure_flexdata_obs_id",
        "exposure_flexdata",
        "exposure",
        ["obs_id"],
        ["exposure_id"],
        source_schema="cdb_latiss",
        referent_schema="cdb_latiss",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        "fk_exposure_flexdata_obs_id", "exposure_flexdata", schema="cdb_latiss", type_="foreignkey"
    )
    op.drop_constraint("fk_ccdexposure_exposure_id", "ccdexposure", schema="cdb_latiss", type_="foreignkey")
    op.drop_constraint(
        "un_ccdexposure_exposure_id_detector", "ccdexposure", schema="cdb_latiss", type_="unique"
    )
    # ### end Alembic commands ###
