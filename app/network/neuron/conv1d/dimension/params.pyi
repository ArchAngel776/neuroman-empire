from typing import TypedDict, Literal

# Types

Conv1dDimensionParam = int

Conv1dDimensionParamsKeyof = Literal["in_channels", "out_channels", "groups", "bias"]


# Main

class Conv1dDimensionParams(TypedDict):
    kernel_size: Conv1dDimensionParam
    stride: Conv1dDimensionParam
    padding: Conv1dDimensionParam
    dilation: Conv1dDimensionParam
