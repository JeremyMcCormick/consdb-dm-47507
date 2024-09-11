"""change primary key to day_obs + seq_num

Revision ID: bf7ed261cc12
Revises: d54a539aad4d
Create Date: 2024-09-11 00:15:16.007496+00:00

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = "bf7ed261cc12"
down_revision: Union[str, None] = "d54a539aad4d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "ccdexposure",
        sa.Column(
            "day_obs",
            sa.INTEGER().with_variant(mysql.INTEGER(), "mysql").with_variant(sa.INTEGER(), "postgresql"),
            nullable=False,
            comment="Day of observation.",
        ),
        schema="cdb_lsstcomcam",
    )
    op.add_column(
        "ccdexposure",
        sa.Column(
            "seq_num",
            sa.INTEGER().with_variant(mysql.INTEGER(), "mysql").with_variant(sa.INTEGER(), "postgresql"),
            nullable=False,
            comment="Sequence number.",
        ),
        schema="cdb_lsstcomcam",
    )
    op.drop_constraint("un_exposure_id_detector", "ccdexposure", schema="cdb_lsstcomcam", type_="unique")
    op.create_unique_constraint(
        "un_ccdexposure_ccdexposure_id", "ccdexposure", ["ccdexposure_id"], schema="cdb_lsstcomcam"
    )
    op.create_unique_constraint(
        "un_ccdexposure_day_obs_seq_num_detector",
        "ccdexposure",
        ["day_obs", "seq_num", "detector"],
        schema="cdb_lsstcomcam",
    )
    op.drop_constraint("fk_exposure_id", "ccdexposure", schema="cdb_lsstcomcam", type_="foreignkey")
    op.create_foreign_key(
        "fk_ccdexposure_day_obs_seq_num",
        "ccdexposure",
        "exposure",
        ["day_obs", "seq_num"],
        ["day_obs", "seq_num"],
        source_schema="cdb_lsstcomcam",
        referent_schema="cdb_lsstcomcam",
    )
    op.add_column(
        "ccdvisit1_quicklook",
        sa.Column(
            "postisr_pixel_median",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Median postISR pixel value.",
        ),
        schema="cdb_lsstcomcam",
    )
    op.drop_constraint("un_day_obs_seq_num", "exposure", schema="cdb_lsstcomcam", type_="unique")
    op.create_unique_constraint(
        "un_exposure_day_obs_seq_num", "exposure", ["day_obs", "seq_num"], schema="cdb_lsstcomcam"
    )
    op.create_unique_constraint(
        "un_exposure_exposure_id", "exposure", ["exposure_id"], schema="cdb_lsstcomcam"
    )
    op.add_column(
        "exposure_flexdata",
        sa.Column(
            "day_obs",
            sa.INTEGER().with_variant(mysql.INTEGER(), "mysql").with_variant(sa.INTEGER(), "postgresql"),
            nullable=False,
            comment="Day of observation.",
        ),
        schema="cdb_lsstcomcam",
    )
    op.add_column(
        "exposure_flexdata",
        sa.Column(
            "seq_num",
            sa.INTEGER().with_variant(mysql.INTEGER(), "mysql").with_variant(sa.INTEGER(), "postgresql"),
            nullable=False,
            comment="Sequence number.",
        ),
        schema="cdb_lsstcomcam",
    )
    op.drop_constraint("fk_obs_id", "exposure_flexdata", schema="cdb_lsstcomcam", type_="foreignkey")
    op.create_foreign_key(
        "fk_exposure_flexdata_day_obs_seq_num",
        "exposure_flexdata",
        "exposure",
        ["day_obs", "seq_num"],
        ["day_obs", "seq_num"],
        source_schema="cdb_lsstcomcam",
        referent_schema="cdb_lsstcomcam",
    )
    op.add_column(
        "visit1_quicklook",
        sa.Column(
            "day_obs",
            sa.INTEGER().with_variant(mysql.INTEGER(), "mysql").with_variant(sa.INTEGER(), "postgresql"),
            nullable=False,
            comment="Day of observation.",
        ),
        schema="cdb_lsstcomcam",
    )
    op.add_column(
        "visit1_quicklook",
        sa.Column(
            "seq_num",
            sa.INTEGER().with_variant(mysql.INTEGER(), "mysql").with_variant(sa.INTEGER(), "postgresql"),
            nullable=False,
            comment="Sequence number.",
        ),
        schema="cdb_lsstcomcam",
    )
    op.add_column(
        "visit1_quicklook",
        sa.Column(
            "postisr_pixel_median_median",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Median postISR pixel value (median across all detectors).",
        ),
        schema="cdb_lsstcomcam",
    )
    op.add_column(
        "visit1_quicklook",
        sa.Column(
            "postisr_pixel_median_mean",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Median postISR pixel value (mean across all detectors).",
        ),
        schema="cdb_lsstcomcam",
    )
    op.add_column(
        "visit1_quicklook",
        sa.Column(
            "postisr_pixel_median_max",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Median postISR pixel value (max across all detectors).",
        ),
        schema="cdb_lsstcomcam",
    )
    op.create_foreign_key(
        "fk_visit1_quicklook_day_obs_seq_num",
        "visit1_quicklook",
        "exposure",
        ["day_obs", "seq_num"],
        ["day_obs", "seq_num"],
        source_schema="cdb_lsstcomcam",
        referent_schema="cdb_lsstcomcam",
    )
    # ### end Alembic commands ###

    # Added by hand: copy day_obs and seq_num into the ccdexposure,
    # exposure_flexdata, and visit1_quicklook tables
    # Extra commands to copy columns from the exposure table
    # and mark the columns as non-null
    pkey = {
        "ccdexposure": "exposure_id",
        "exposure_flexdata": "obs_id",
        "visit1_quicklook": "visit_id",
    }
    the_schema = "cdb_lsstcomcam"
    for destination_table in ("ccdexposure", "exposure_flexdata", "visit1_quicklook"):
        for column in ("day_obs", "seq_num"):
            op.execute(
                f"""
                    UPDATE {the_schema}.{destination_table}
                        SET {column} = {the_schema}.exposure.{column}
                        FROM {the_schema}.exposure
                        WHERE {the_schema}.exposure.exposure_id =
                            {the_schema}.{destination_table}.{pkey[destination_table]}
                """
            )
            op.alter_column(destination_table, column, nullable=False, schema=the_schema)


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        "fk_visit1_quicklook_day_obs_seq_num", "visit1_quicklook", schema="cdb_lsstcomcam", type_="foreignkey"
    )
    op.drop_column("visit1_quicklook", "postisr_pixel_median_max", schema="cdb_lsstcomcam")
    op.drop_column("visit1_quicklook", "postisr_pixel_median_mean", schema="cdb_lsstcomcam")
    op.drop_column("visit1_quicklook", "postisr_pixel_median_median", schema="cdb_lsstcomcam")
    op.drop_column("visit1_quicklook", "seq_num", schema="cdb_lsstcomcam")
    op.drop_column("visit1_quicklook", "day_obs", schema="cdb_lsstcomcam")
    op.drop_constraint(
        "fk_exposure_flexdata_day_obs_seq_num",
        "exposure_flexdata",
        schema="cdb_lsstcomcam",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "fk_obs_id",
        "exposure_flexdata",
        "exposure",
        ["obs_id"],
        ["exposure_id"],
        source_schema="cdb_lsstcomcam",
        referent_schema="cdb_lsstcomcam",
    )
    op.drop_column("exposure_flexdata", "seq_num", schema="cdb_lsstcomcam")
    op.drop_column("exposure_flexdata", "day_obs", schema="cdb_lsstcomcam")
    op.drop_constraint("un_exposure_exposure_id", "exposure", schema="cdb_lsstcomcam", type_="unique")
    op.drop_constraint("un_exposure_day_obs_seq_num", "exposure", schema="cdb_lsstcomcam", type_="unique")
    op.create_unique_constraint(
        "un_day_obs_seq_num", "exposure", ["day_obs", "seq_num"], schema="cdb_lsstcomcam"
    )
    op.drop_column("ccdvisit1_quicklook", "postisr_pixel_median", schema="cdb_lsstcomcam")
    op.drop_constraint(
        "fk_ccdexposure_day_obs_seq_num", "ccdexposure", schema="cdb_lsstcomcam", type_="foreignkey"
    )
    op.create_foreign_key(
        "fk_exposure_id",
        "ccdexposure",
        "exposure",
        ["exposure_id"],
        ["exposure_id"],
        source_schema="cdb_lsstcomcam",
        referent_schema="cdb_lsstcomcam",
    )
    op.drop_constraint(
        "un_ccdexposure_day_obs_seq_num_detector", "ccdexposure", schema="cdb_lsstcomcam", type_="unique"
    )
    op.drop_constraint(
        "un_ccdexposure_ccdexposure_id", "ccdexposure", schema="cdb_lsstcomcam", type_="unique"
    )
    op.create_unique_constraint(
        "un_exposure_id_detector", "ccdexposure", ["exposure_id", "detector"], schema="cdb_lsstcomcam"
    )
    op.drop_column("ccdexposure", "seq_num", schema="cdb_lsstcomcam")
    op.drop_column("ccdexposure", "day_obs", schema="cdb_lsstcomcam")
    # ### end Alembic commands ###
