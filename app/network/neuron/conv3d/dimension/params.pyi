from typing import TypedDict, Literal

# Types

Conv3dDimensionParam = int | tuple[int, int, int]

Conv3dDimensionParamsKeyof = Literal["kernel_size", "stride", "padding", "dilation"]


# Main

class Conv3dDimensionParams(TypedDict):
    kernel_size: Conv3dDimensionParam
    stride: Conv3dDimensionParam
    padding: Conv3dDimensionParam
    dilation: Conv3dDimensionParam
