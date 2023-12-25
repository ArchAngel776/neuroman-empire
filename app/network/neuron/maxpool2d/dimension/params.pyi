from typing import TypedDict, Literal

# Types

MaxPool2dDimensionParam = int | tuple[int, int]

MaxPool2dDimensionParamsKeyof = Literal["kernel_size", "stride", "padding", "dilation"]


# Main

class MaxPool2dDimensionParams(TypedDict):
    kernel_size: MaxPool2dDimensionParam
    stride: MaxPool2dDimensionParam
    padding: MaxPool2dDimensionParam
    dilation: MaxPool2dDimensionParam
