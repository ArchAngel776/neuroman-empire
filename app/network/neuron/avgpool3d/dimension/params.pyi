from typing import TypedDict, Literal

# Types

AvgPool3dDimensionParam = int | tuple[int, int, int]

AvgPool3dDimensionParamsKeyof = Literal["kernel_size", "stride", "padding"]


# Main

class AvgPool3dDimensionParams(TypedDict):
    kernel_size: AvgPool3dDimensionParam
    stride: AvgPool3dDimensionParam
    padding: AvgPool3dDimensionParam
