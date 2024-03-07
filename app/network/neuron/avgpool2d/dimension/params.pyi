from typing import TypedDict, Literal

# Types

AvgPool2dDimensionParam = int | tuple[int, int]

AvgPool2dDimensionParamsKeyof = Literal["kernel_size", "stride", "padding"]


# Main

class AvgPool2dDimensionParams(TypedDict):
    kernel_size: AvgPool2dDimensionParam
    stride: AvgPool2dDimensionParam
    padding: AvgPool2dDimensionParam
