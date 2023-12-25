from typing import TypedDict, Literal

# Types

MaxPool3dDimensionParam = int | tuple[int, int, int]

MaxPool3dDimensionParamsKeyof = Literal["kernel_size", "stride", "padding", "dilation"]


# Main

class MaxPool3dDimensionParams(TypedDict):
    kernel_size: MaxPool3dDimensionParam
    stride: MaxPool3dDimensionParam
    padding: MaxPool3dDimensionParam
    dilation: MaxPool3dDimensionParam
