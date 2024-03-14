from typing import TypedDict, Literal

# Types

AdaptiveAvgPool1dDimensionParam = int

AdaptiveAvgPool1dDimensionParamsKeyof = Literal["output_size"]


# Main

class AdaptiveAvgPool1dDimensionParams(TypedDict):
    output_size: AdaptiveAvgPool1dDimensionParam