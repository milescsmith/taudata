from collections.abc import Sequence
from pathlib import Path

import anndata as ad
import polars as pl


def read_processed_olink_parquet(
    file: Path,
    X_col: str,
    sampleid_col: str,
    extra_obs_cols: Sequence[str] | None = None,
    extra_var_cols: Sequence[str] | None = None,
    extra_uns_keys: Sequence[str] | None = None,
    extra_layer_keys: Sequence[str] | None = None,
) -> ad.AnnData:
    """Import an existing processed Olink dataset stored in a parquet file and convert it to an AnnData object

    This function is for use when dealing with level2 or higher data, NOT for import of
    data coming directly from NPX software


    Parameters
    ----------
    file : Path
        Path to the parquet file to import
    X_col : str
        Column in the dataframe to use as the X matrix
    sampledid_col : str
        Column in the dataframe to use when grouping Assays for a particular sample
    extra_obs_cols : Sequence[str], optional
        Additional columns that may be present in the incoming parquet file that should be stored in `obs`
    extra_var_cols : Sequence[str], optional
        Additional columns that may be present in the incoming parquet file that should be stored in `var`
    extra_uns_keys : Sequence[str], optional
        Additional columns that may be present in the incoming parquet file that should be stored in `uns`
    extra_layer_keys : Sequence[str], optional
        Additional columns that may be present in the incoming parquet file that should be stored in `layers`

    Returns
    -------
    ad.AnnData

    Notes
    -----
    Work in progress. Currently it stores data according to the following
        * var: "Assay", "UniProt", "OlinkID", "Panel","AssayType", "Block", "AssayQC", "high_var_assay",
            "assay_level_qc", "Block", "AssayQC", "IntraCV", "InterCV","AssayQCWarn"
        * obs: "SubjectRef", "Assay_Sample_ID", "SampleID", "SampleType", "SampleQC", "InstrumentType", "Project",
            "KitLot", "PCLot", "SCLot", "NCLot", "AssayTechIssue", "UniqueID", "Median", "Variance", "ReferenceMedian"
        * uns: "Assay_Filename", "Analyte_Failure_Pct", "Analyte_Warn_Pct", "Plating_Notes", "PlateID",
            "DataAnalysisRefID", "Panel", "Normalization", "SoftwareVersion", "SoftwareName", "PanelDataArchiveVersion",
            "PreProcessingVersion",
        * layers: "WellID", "ExtNPX", "NPX", "ExtNPC_Corrected", "LogProtExp", "LogProtExp_Raw", "Correction",
            "PCNormalizedNPX", "SampleBlockQCWarn", "SampleBlockQCFail", "BlockQCFail", "sample_level_qc",

    """
    var_cols = [
        "Assay",
        "UniProt",
        "OlinkID",
        "Panel",
        "AssayType",
        "Block",
        "AssayQC",
        "high_var_assay",
        "assay_level_qc",
        "Block",
        "AssayQC",
        "IntraCV",
        "InterCV",
        "AssayQCWarn",
    ]

    obs_cols = [
        "SubjectRef",
        "Assay_Sample_ID",
        "SampleID",
        "SampleType",
        "SampleQC",
        "InstrumentType",
        "Project",
        "KitLot",
        "PCLot",
        "SCLot",
        "NCLot",
        "AssayTechIssue",
        "UniqueID",
        "Median",
        "Variance",
        "ReferenceMedian",
    ]

    uns_keys = [
        "Assay_Filename",
        "Analyte_Failure_Pct",
        "Analyte_Warn_Pct",
        "Plating_Notes",
        "PlateID",
        "DataAnalysisRefID",
        "Panel",
        "Normalization",
        "SoftwareVersion",  # maybe this should be in obs; may need somewhere to stuff a normalization factor dictionary for objects arising from mixed Olink runs
        "SoftwareName",
        "PanelDataArchiveVersion",
        "PreProcessingVersion",
    ]

    # several of these I'm currently storing as a layer because I'm afraid of a situation
    # where a patient sample has their assays arising from multiple different Olink runs
    layer_keys = [
        "WellID",
        "ExtNPX",
        "NPX",
        "ExtNPC_Corrected",
        "LogProtExp",
        "LogProtExp_Raw",
        "Correction",
        "PCNormalizedNPX",
        "SampleBlockQCWarn",
        "SampleBlockQCFail",
        "BlockQCFail",
        "sample_level_qc",
    ]

    var_cols = [*var_cols, extra_var_cols] if extra_var_cols else var_cols
    obs_cols = [*obs_cols, extra_obs_cols] if extra_obs_cols else obs_cols
    obs_cols = obs_cols if sampleid_col in obs_cols else [*obs_cols, sampleid_col]
    uns_keys = [*uns_keys, extra_uns_keys] if extra_uns_keys else uns_keys
    layer_keys = [*layer_keys, extra_layer_keys] if extra_layer_keys else layer_keys

    # import parquet
    olink_df = pl.read_parquet(file)
    if X_col not in olink_df.columns:
        msg = f"{X_col} was not found in the columns of the passed file"
        raise pl.exceptions.ColumnNotFoundError(msg)

    var_df = (
        olink_df.select([pl.col(_) for _ in olink_df.columns if _ in var_cols])
        .unique(maintain_order=True)
        .to_pandas()
        .set_index("Assay")
    )
    obs_df = (
        olink_df.select([pl.col(_) for _ in olink_df.columns if _ in obs_cols])
        .unique(maintain_order=True)
        .to_pandas()
        .set_index(sampleid_col)
    )

    uns_dict = {k: olink_df[k].to_list() for k in uns_keys if k in olink_df.columns}

    layers_dict = {
        k: olink_df.select(pl.col(sampleid_col), pl.col("Assay"), pl.col(k))  # pyright: ignore[reportArgumentType] pyright doesn't know what the fuck it is talking about
        .pivot(on="Assay", index=sampleid_col, values=k)
        .drop(pl.col(sampleid_col))  # pyright: ignore[reportArgumentType]
        .to_numpy()
        for k in layer_keys
        if k in olink_df.columns
    }

    adata = ad.AnnData(X=layers_dict[X_col], obs=obs_df, var=var_df, uns=uns_dict, layers=layers_dict)

    return adata
