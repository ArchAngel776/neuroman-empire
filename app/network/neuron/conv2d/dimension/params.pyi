from typing import TypedDict, Literal

# Types

Conv2dDimensionParam = int | tuple[int, int]

Conv2dDimensionParamsKeyof = Literal["kernel_size", "stride", "padding", "dilation"]


# Main

class Conv2dDimensionParams(TypedDict):
    kernel_size: Conv2dDimensionParam
    stride: Conv2dDimensionParam
    padding: Conv2dDimensionParam
    dilation: Conv2dDimensionParam
