from collections.abc import Callable
from typing import Annotated, Any, Literal

from annotated_types import Ge, Le
from pydantic import BaseModel, GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import core_schema
from semver import Version


class _VersionPydanticAnnotation:
    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        _source_type: Any,
        _handler: Callable[[Any], core_schema.CoreSchema],
    ) -> core_schema.CoreSchema:
        def validate_from_str(value: str) -> Version:
            return Version.parse(value)

        from_str_schema = core_schema.chain_schema(
            [
                core_schema.str_schema(),
                core_schema.no_info_plain_validator_function(validate_from_str),
            ]
        )

        return core_schema.json_or_python_schema(
            json_schema=from_str_schema,
            python_schema=core_schema.union_schema(
                [
                    core_schema.is_instance_schema(Version),
                    from_str_schema,
                ]
            ),
            serialization=core_schema.to_string_ser_schema(),
        )

    @classmethod
    def __get_pydantic_json_schema__(
        cls, _core_schema: core_schema.CoreSchema, handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:
        return handler(core_schema.str_schema())


ManifestVersion = Annotated[Version, _VersionPydanticAnnotation]


class Olink_L1(BaseModel):
    SampleID: str
    SampleType: str
    WellID: str
    PlateID: str
    DataAnalysisRefID: str
    OlinkID: str
    Uniprot: str
    Assay: str
    AssayType: str
    Panel: str
    Block: str
    Count: int
    ExtNPX: float
    NPX: float
    Normalization: str
    PCNormalizedNPX: float
    AssayQC: str
    SampleQC: str
    SoftwareVersion: _VersionPydanticAnnotation
    SoftwareName: Literal["NPX Map", "NPX Map CLI"]
    PanelDataArchiveVersion: _VersionPydanticAnnotation
    PreProcessingVersion: _VersionPydanticAnnotation
    PreProcessingSoftware: Literal["NPX Map CLI", "NPX Map", "ngs2counts"]
    InstrumentType: Literal[
        "Element Biosciences AVITI",
        "MGI Tech DNBSEQ T7",
        "Illumina NextSeq 550",
        "Illumina NextSeq 1000",
        "Illumina NextSeq 2000",
        "Illumina NovaSeq 6000",
        "Illumina NovaSeq X",
        "Illumina NovaSeq X Plus",
        "Ultima Genomics UG100",
    ]  # should this just be an enum?
    IntraCV: float
    InterCV: float
    SampleBlockQCWarn: Annotated[int, Ge(0), Le(1)]
    SampleBlockQCFail: Annotated[int, Ge(0), Le(1)]
    AssayQCWarn: Annotated[int, Ge(0), Le(1)]
    Project: str
    KitLot: str  # this must have some sort of version format schema?
    PCLot: str  # ditto
    SCLot: str  # again
    NCLot: str  # yet again
    AssayTechIssue: str
    UniqueID: str  # need Plate#-Well#-SampleID schema


class Olink_L2(Olink_L1):
    Median: float
    Variance: float
    ReferenceMedian: float
    Correction: float
    ExtNPX_Corrected: float
    LogProtExp: float
    LogProtExp_Raw: float
    high_var_assay: Literal["Pass", "High-variant assay"]
    sample_level_qc: Literal["Pass", "Below LLOD", "Below LLOQ"]
    assay_level_qc: Literal["Continuous", "Semi-continuous", "Categorical"]
