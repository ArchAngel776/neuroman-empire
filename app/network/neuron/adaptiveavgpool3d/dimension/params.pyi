from typing import TypedDict, Literal

# Types

AdaptiveAvgPool3dDimensionParam = int | tuple[int, int, int]

AdaptiveAvgPool3dDimensionParamsKeyof = Literal["output_size"]


# Main

class AdaptiveAvgPool3dDimensionParams(TypedDict):
    output_size: AdaptiveAvgPool3dDimensionParam
