from typing import TypedDict, Literal

# Types

MaxPool1dDimensionParam = int

MaxPool1dDimensionParamsKeyof = Literal["kernel_size", "stride", "padding", "dilation"]


# Main

class MaxPool1dDimensionParams(TypedDict):
    kernel_size: MaxPool1dDimensionParam
    stride: MaxPool1dDimensionParam
    padding: MaxPool1dDimensionParam
    dilation: MaxPool1dDimensionParam
