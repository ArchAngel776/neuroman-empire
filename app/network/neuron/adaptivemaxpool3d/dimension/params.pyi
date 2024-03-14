from typing import TypedDict, Literal

# Types

AdaptiveMaxPool3dDimensionParam = int | tuple[int, int, int]

AdaptiveMaxPool3dDimensionParamsKeyof = Literal["output_size"]


# Main

class AdaptiveMaxPool3dDimensionParams(TypedDict):
    output_size: AdaptiveMaxPool3dDimensionParam
