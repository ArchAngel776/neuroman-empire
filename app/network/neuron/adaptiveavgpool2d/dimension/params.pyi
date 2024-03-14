from typing import TypedDict, Literal

# Types

AdaptiveAvgPool2dDimensionParam = int | tuple[int, int]

AdaptiveAvgPool2dDimensionParamsKeyof = Literal["output_size"]


# Main

class AdaptiveAvgPool2dDimensionParams(TypedDict):
    output_size: AdaptiveAvgPool2dDimensionParam
