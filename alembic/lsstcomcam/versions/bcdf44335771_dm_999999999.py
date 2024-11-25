"""DM-999999999

Revision ID: bcdf44335771
Revises: 0490d793fc1a
Create Date: 2024-11-25 21:18:35.867286+00:00

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = "bcdf44335771"
down_revision: Union[str, None] = "0490d793fc1a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "exposure_quicklook",
        sa.Column(
            "exposure_id",
            sa.BIGINT().with_variant(mysql.BIGINT(), "mysql").with_variant(sa.BIGINT(), "postgresql"),
            nullable=False,
            comment="Unique identifier.",
        ),
        sa.Column(
            "day_obs",
            sa.INTEGER().with_variant(mysql.INTEGER(), "mysql").with_variant(sa.INTEGER(), "postgresql"),
            nullable=False,
            comment="Day of observation.",
        ),
        sa.Column(
            "seq_num",
            sa.INTEGER().with_variant(mysql.INTEGER(), "mysql").with_variant(sa.INTEGER(), "postgresql"),
            nullable=False,
            comment="Sequence number.",
        ),
        sa.Column(
            "postisr_pixel_median_median",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Median postISR pixel value (median across all detectors).",
        ),
        sa.Column(
            "postisr_pixel_median_mean",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Median postISR pixel value (mean across all detectors).",
        ),
        sa.Column(
            "postisr_pixel_median_max",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Median postISR pixel value (max across all detectors).",
        ),
        sa.Column(
            "mount_motion_image_degradation",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Image degradation due to mount motion.",
        ),
        sa.Column(
            "mount_motion_image_degradation_az",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Image degradation due to mount motion in azimuth.",
        ),
        sa.Column(
            "mount_motion_image_degradation_rot",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Image degradation due to rotator jitter.",
        ),
        sa.Column(
            "mount_jitter_rms",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="RMS mount jitter.",
        ),
        sa.Column(
            "mount_jitter_rms_az",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Azimuth RMS mount jitter.",
        ),
        sa.Column(
            "mount_jitter_rms_el",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Elevation RMS mount jitter.",
        ),
        sa.Column(
            "mount_jitter_rms_rot",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Rotator RMS mount jitter.",
        ),
        sa.ForeignKeyConstraint(
            ["day_obs", "seq_num"],
            ["cdb_lsstcomcam.exposure.day_obs", "cdb_lsstcomcam.exposure.seq_num"],
            name="fk_exposure_quicklook_day_obs_seq_num",
        ),
        sa.ForeignKeyConstraint(
            ["exposure_id"], ["cdb_lsstcomcam.exposure.exposure_id"], name="fk_exposure_quicklook_obs_id"
        ),
        sa.PrimaryKeyConstraint("day_obs", "seq_num"),
        schema="cdb_lsstcomcam",
        mysql_engine="MyISAM",
    )
    op.create_table(
        "ccdexposure_quicklook",
        sa.Column(
            "ccdexposure_id",
            sa.BIGINT().with_variant(mysql.BIGINT(), "mysql").with_variant(sa.BIGINT(), "postgresql"),
            nullable=False,
            comment="Unique identifier.",
        ),
        sa.Column(
            "postisr_pixel_median",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Median postISR pixel value.",
        ),
        sa.ForeignKeyConstraint(
            ["ccdexposure_id"],
            ["cdb_lsstcomcam.ccdexposure.ccdexposure_id"],
            name="fk_ccdexposure_quicklook_obs_id",
        ),
        sa.PrimaryKeyConstraint("ccdexposure_id"),
        schema="cdb_lsstcomcam",
        mysql_engine="MyISAM",
    )
    op.add_column(
        "ccdvisit1_quicklook",
        sa.Column(
            "pixel_scale",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Measured detector pixel scale.",
        ),
        schema="cdb_lsstcomcam",
    )
    op.add_column(
        "ccdvisit1_quicklook",
        sa.Column(
            "stats_mag_lim",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Magnitude limit at fixed SNR (default SNR=5) calculated from exposure summary stats.",
        ),
        schema="cdb_lsstcomcam",
    )
    op.add_column(
        "ccdvisit1_quicklook",
        sa.Column(
            "psf_ap_flux_delta",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Delta (max - min) of model psf aperture flux (with aperture radius of max(2, 3*psfSigma)) values evaluated on a grid of unmasked pixels.",
        ),
        schema="cdb_lsstcomcam",
    )
    op.add_column(
        "ccdvisit1_quicklook",
        sa.Column(
            "psf_ap_corr_sigma_scaled_delta",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Delta (max - min) of psf flux aperture correction factors scaled (divided) by the psfSigma evaluated on a grid of unmasked pixels.",
        ),
        schema="cdb_lsstcomcam",
    )
    op.drop_column("ccdvisit1_quicklook", "postisr_pixel_median", schema="cdb_lsstcomcam")
    op.add_column(
        "visit1_quicklook",
        sa.Column(
            "pixel_scale_min",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Measured detector pixel scale (minimum across all detectors).",
        ),
        schema="cdb_lsstcomcam",
    )
    op.add_column(
        "visit1_quicklook",
        sa.Column(
            "pixel_scale_max",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Measured detector pixel scale (maximum across all detectors).",
        ),
        schema="cdb_lsstcomcam",
    )
    op.add_column(
        "visit1_quicklook",
        sa.Column(
            "pixel_scale_median",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Measured detector pixel scale (median across all detectors).",
        ),
        schema="cdb_lsstcomcam",
    )
    op.add_column(
        "visit1_quicklook",
        sa.Column(
            "stats_mag_lim_min",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Magnitude limit at fixed SNR (default SNR=5) calculated from exposure summary stats (minimum across all detectors).",
        ),
        schema="cdb_lsstcomcam",
    )
    op.add_column(
        "visit1_quicklook",
        sa.Column(
            "stats_mag_lim_max",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Magnitude limit at fixed SNR (default SNR=5) calculated from exposure summary stats (maximum across all detectors).",
        ),
        schema="cdb_lsstcomcam",
    )
    op.add_column(
        "visit1_quicklook",
        sa.Column(
            "stats_mag_lim_median",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Magnitude limit at fixed SNR (default SNR=5) calculated from exposure summary stats (median across all detectors).",
        ),
        schema="cdb_lsstcomcam",
    )
    op.add_column(
        "visit1_quicklook",
        sa.Column(
            "psf_ap_flux_delta_min",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Delta (max - min) of model psf aperture flux (with aperture radius of max(2, 3*psfSigma)) values evaluated on a grid of unmasked pixels (minimum across all detectors).",
        ),
        schema="cdb_lsstcomcam",
    )
    op.add_column(
        "visit1_quicklook",
        sa.Column(
            "psf_ap_flux_delta_max",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Delta (max - min) of model psf aperture flux (with aperture radius of max(2, 3*psfSigma)) values evaluated on a grid of unmasked pixels (maximum across all detectors).",
        ),
        schema="cdb_lsstcomcam",
    )
    op.add_column(
        "visit1_quicklook",
        sa.Column(
            "psf_ap_flux_delta_median",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Delta (max - min) of model psf aperture flux (with aperture radius of max(2, 3*psfSigma)) values evaluated on a grid of unmasked pixels (median across all detectors).",
        ),
        schema="cdb_lsstcomcam",
    )
    op.add_column(
        "visit1_quicklook",
        sa.Column(
            "psf_ap_corr_sigma_scaled_delta_min",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Delta (max - min) of psf flux aperture correction factors scaled (divided) by the psfSigma evaluated on a grid of unmasked pixels (minimum across all detectors).",
        ),
        schema="cdb_lsstcomcam",
    )
    op.add_column(
        "visit1_quicklook",
        sa.Column(
            "psf_ap_corr_sigma_scaled_delta_max",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Delta (max - min) of psf flux aperture correction factors scaled (divided) by the psfSigma evaluated on a grid of unmasked pixels (maximum across all detectors).",
        ),
        schema="cdb_lsstcomcam",
    )
    op.add_column(
        "visit1_quicklook",
        sa.Column(
            "psf_ap_corr_sigma_scaled_delta_median",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Delta (max - min) of psf flux aperture correction factors scaled (divided) by the psfSigma evaluated on a grid of unmasked pixels (median across all detectors).",
        ),
        schema="cdb_lsstcomcam",
    )
    op.drop_column("visit1_quicklook", "postisr_pixel_median_median", schema="cdb_lsstcomcam")
    op.drop_column("visit1_quicklook", "postisr_pixel_median_mean", schema="cdb_lsstcomcam")
    op.drop_column("visit1_quicklook", "postisr_pixel_median_max", schema="cdb_lsstcomcam")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "visit1_quicklook",
        sa.Column(
            "postisr_pixel_median_max",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=True,
            comment="Median postISR pixel value (max across all detectors).",
        ),
        schema="cdb_lsstcomcam",
    )
    op.add_column(
        "visit1_quicklook",
        sa.Column(
            "postisr_pixel_median_mean",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=True,
            comment="Median postISR pixel value (mean across all detectors).",
        ),
        schema="cdb_lsstcomcam",
    )
    op.add_column(
        "visit1_quicklook",
        sa.Column(
            "postisr_pixel_median_median",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=True,
            comment="Median postISR pixel value (median across all detectors).",
        ),
        schema="cdb_lsstcomcam",
    )
    op.drop_column("visit1_quicklook", "psf_ap_corr_sigma_scaled_delta_median", schema="cdb_lsstcomcam")
    op.drop_column("visit1_quicklook", "psf_ap_corr_sigma_scaled_delta_max", schema="cdb_lsstcomcam")
    op.drop_column("visit1_quicklook", "psf_ap_corr_sigma_scaled_delta_min", schema="cdb_lsstcomcam")
    op.drop_column("visit1_quicklook", "psf_ap_flux_delta_median", schema="cdb_lsstcomcam")
    op.drop_column("visit1_quicklook", "psf_ap_flux_delta_max", schema="cdb_lsstcomcam")
    op.drop_column("visit1_quicklook", "psf_ap_flux_delta_min", schema="cdb_lsstcomcam")
    op.drop_column("visit1_quicklook", "stats_mag_lim_median", schema="cdb_lsstcomcam")
    op.drop_column("visit1_quicklook", "stats_mag_lim_max", schema="cdb_lsstcomcam")
    op.drop_column("visit1_quicklook", "stats_mag_lim_min", schema="cdb_lsstcomcam")
    op.drop_column("visit1_quicklook", "pixel_scale_median", schema="cdb_lsstcomcam")
    op.drop_column("visit1_quicklook", "pixel_scale_max", schema="cdb_lsstcomcam")
    op.drop_column("visit1_quicklook", "pixel_scale_min", schema="cdb_lsstcomcam")
    op.add_column(
        "ccdvisit1_quicklook",
        sa.Column(
            "postisr_pixel_median",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=True,
            comment="Median postISR pixel value.",
        ),
        schema="cdb_lsstcomcam",
    )
    op.drop_column("ccdvisit1_quicklook", "psf_ap_corr_sigma_scaled_delta", schema="cdb_lsstcomcam")
    op.drop_column("ccdvisit1_quicklook", "psf_ap_flux_delta", schema="cdb_lsstcomcam")
    op.drop_column("ccdvisit1_quicklook", "stats_mag_lim", schema="cdb_lsstcomcam")
    op.drop_column("ccdvisit1_quicklook", "pixel_scale", schema="cdb_lsstcomcam")
    op.drop_table("ccdexposure_quicklook", schema="cdb_lsstcomcam")
    op.drop_table("exposure_quicklook", schema="cdb_lsstcomcam")
    # ### end Alembic commands ###
