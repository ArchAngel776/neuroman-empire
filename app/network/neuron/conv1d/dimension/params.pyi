from typing import TypedDict, Literal

# Types

Conv1dDimensionParam = int

Conv1dDimensionParamsKeyof = Literal["kernel_size", "stride", "padding", "dilation"]


# Main

class Conv1dDimensionParams(TypedDict):
    kernel_size: Conv1dDimensionParam
    stride: Conv1dDimensionParam
    padding: Conv1dDimensionParam
    dilation: Conv1dDimensionParam
