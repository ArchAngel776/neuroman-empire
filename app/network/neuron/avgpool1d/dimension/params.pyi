from typing import TypedDict, Literal

# Types

AvgPool1dDimensionParam = int

AvgPool1dDimensionParamsKeyof = Literal["kernel_size", "stride", "padding"]


# Main

class AvgPool1dDimensionParams(TypedDict):
    kernel_size: AvgPool1dDimensionParam
    stride: AvgPool1dDimensionParam
    padding: AvgPool1dDimensionParam
