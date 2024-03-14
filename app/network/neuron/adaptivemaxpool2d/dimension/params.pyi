from typing import TypedDict, Literal

# Types

AdaptiveMaxPool2dDimensionParam = int | tuple[int, int]

AdaptiveMaxPool2dDimensionParamsKeyof = Literal["output_size"]


# Main

class AdaptiveMaxPool2dDimensionParams(TypedDict):
    output_size: AdaptiveMaxPool2dDimensionParam
