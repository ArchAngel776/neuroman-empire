from typing import TypedDict, Literal

# Types

AdaptiveMaxPool1dDimensionParam = int

AdaptiveMaxPool1dDimensionParamsKeyof = Literal["output_size"]


# Main

class AdaptiveMaxPool1dDimensionParams(TypedDict):
    output_size: AdaptiveMaxPool1dDimensionParam