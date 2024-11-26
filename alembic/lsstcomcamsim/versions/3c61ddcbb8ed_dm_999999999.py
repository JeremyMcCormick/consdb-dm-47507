"""DM-999999999

Revision ID: 3c61ddcbb8ed
Revises: cff7da7ec8ed
Create Date: 2024-11-26 00:29:53.539394+00:00

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = "3c61ddcbb8ed"
down_revision: Union[str, None] = "cff7da7ec8ed"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "ccdvisit1_quicklook",
        sa.Column(
            "pixel_scale",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Measured detector pixel scale.",
        ),
        schema="cdb_lsstcomcamsim",
    )
    op.add_column(
        "ccdvisit1_quicklook",
        sa.Column(
            "stats_mag_lim",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Magnitude limit at fixed SNR (default SNR=5) calculated from exposure summary stats.",
        ),
        schema="cdb_lsstcomcamsim",
    )
    op.add_column(
        "ccdvisit1_quicklook",
        sa.Column(
            "psf_ap_flux_delta",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Delta (max - min) of model psf aperture flux (with aperture radius of max(2, 3*psfSigma)) values evaluated on a grid of unmasked pixels.",
        ),
        schema="cdb_lsstcomcamsim",
    )
    op.add_column(
        "ccdvisit1_quicklook",
        sa.Column(
            "psf_ap_corr_sigma_scaled_delta",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Delta (max - min) of psf flux aperture correction factors scaled (divided) by the psfSigma evaluated on a grid of unmasked pixels.",
        ),
        schema="cdb_lsstcomcamsim",
    )
    op.add_column(
        "visit1_quicklook",
        sa.Column(
            "pixel_scale_min",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Measured detector pixel scale (minimum across all detectors).",
        ),
        schema="cdb_lsstcomcamsim",
    )
    op.add_column(
        "visit1_quicklook",
        sa.Column(
            "pixel_scale_max",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Measured detector pixel scale (maximum across all detectors).",
        ),
        schema="cdb_lsstcomcamsim",
    )
    op.add_column(
        "visit1_quicklook",
        sa.Column(
            "pixel_scale_median",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Measured detector pixel scale (median across all detectors).",
        ),
        schema="cdb_lsstcomcamsim",
    )
    op.add_column(
        "visit1_quicklook",
        sa.Column(
            "stats_mag_lim_min",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Magnitude limit at fixed SNR (default SNR=5) calculated from exposure summary stats (minimum across all detectors).",
        ),
        schema="cdb_lsstcomcamsim",
    )
    op.add_column(
        "visit1_quicklook",
        sa.Column(
            "stats_mag_lim_max",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Magnitude limit at fixed SNR (default SNR=5) calculated from exposure summary stats (maximum across all detectors).",
        ),
        schema="cdb_lsstcomcamsim",
    )
    op.add_column(
        "visit1_quicklook",
        sa.Column(
            "stats_mag_lim_median",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Magnitude limit at fixed SNR (default SNR=5) calculated from exposure summary stats (median across all detectors).",
        ),
        schema="cdb_lsstcomcamsim",
    )
    op.add_column(
        "visit1_quicklook",
        sa.Column(
            "psf_ap_flux_delta_min",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Delta (max - min) of model psf aperture flux (with aperture radius of max(2, 3*psfSigma)) values evaluated on a grid of unmasked pixels (minimum across all detectors).",
        ),
        schema="cdb_lsstcomcamsim",
    )
    op.add_column(
        "visit1_quicklook",
        sa.Column(
            "psf_ap_flux_delta_max",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Delta (max - min) of model psf aperture flux (with aperture radius of max(2, 3*psfSigma)) values evaluated on a grid of unmasked pixels (maximum across all detectors).",
        ),
        schema="cdb_lsstcomcamsim",
    )
    op.add_column(
        "visit1_quicklook",
        sa.Column(
            "psf_ap_flux_delta_median",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Delta (max - min) of model psf aperture flux (with aperture radius of max(2, 3*psfSigma)) values evaluated on a grid of unmasked pixels (median across all detectors).",
        ),
        schema="cdb_lsstcomcamsim",
    )
    op.add_column(
        "visit1_quicklook",
        sa.Column(
            "psf_ap_corr_sigma_scaled_delta_min",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Delta (max - min) of psf flux aperture correction factors scaled (divided) by the psfSigma evaluated on a grid of unmasked pixels (minimum across all detectors).",
        ),
        schema="cdb_lsstcomcamsim",
    )
    op.add_column(
        "visit1_quicklook",
        sa.Column(
            "psf_ap_corr_sigma_scaled_delta_max",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Delta (max - min) of psf flux aperture correction factors scaled (divided) by the psfSigma evaluated on a grid of unmasked pixels (maximum across all detectors).",
        ),
        schema="cdb_lsstcomcamsim",
    )
    op.add_column(
        "visit1_quicklook",
        sa.Column(
            "psf_ap_corr_sigma_scaled_delta_median",
            sa.FLOAT().with_variant(mysql.FLOAT(), "mysql").with_variant(sa.FLOAT(), "postgresql"),
            nullable=True,
            comment="Delta (max - min) of psf flux aperture correction factors scaled (divided) by the psfSigma evaluated on a grid of unmasked pixels (median across all detectors).",
        ),
        schema="cdb_lsstcomcamsim",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("visit1_quicklook", "psf_ap_corr_sigma_scaled_delta_median", schema="cdb_lsstcomcamsim")
    op.drop_column("visit1_quicklook", "psf_ap_corr_sigma_scaled_delta_max", schema="cdb_lsstcomcamsim")
    op.drop_column("visit1_quicklook", "psf_ap_corr_sigma_scaled_delta_min", schema="cdb_lsstcomcamsim")
    op.drop_column("visit1_quicklook", "psf_ap_flux_delta_median", schema="cdb_lsstcomcamsim")
    op.drop_column("visit1_quicklook", "psf_ap_flux_delta_max", schema="cdb_lsstcomcamsim")
    op.drop_column("visit1_quicklook", "psf_ap_flux_delta_min", schema="cdb_lsstcomcamsim")
    op.drop_column("visit1_quicklook", "stats_mag_lim_median", schema="cdb_lsstcomcamsim")
    op.drop_column("visit1_quicklook", "stats_mag_lim_max", schema="cdb_lsstcomcamsim")
    op.drop_column("visit1_quicklook", "stats_mag_lim_min", schema="cdb_lsstcomcamsim")
    op.drop_column("visit1_quicklook", "pixel_scale_median", schema="cdb_lsstcomcamsim")
    op.drop_column("visit1_quicklook", "pixel_scale_max", schema="cdb_lsstcomcamsim")
    op.drop_column("visit1_quicklook", "pixel_scale_min", schema="cdb_lsstcomcamsim")
    op.drop_column("ccdvisit1_quicklook", "psf_ap_corr_sigma_scaled_delta", schema="cdb_lsstcomcamsim")
    op.drop_column("ccdvisit1_quicklook", "psf_ap_flux_delta", schema="cdb_lsstcomcamsim")
    op.drop_column("ccdvisit1_quicklook", "stats_mag_lim", schema="cdb_lsstcomcamsim")
    op.drop_column("ccdvisit1_quicklook", "pixel_scale", schema="cdb_lsstcomcamsim")
    # ### end Alembic commands ###
