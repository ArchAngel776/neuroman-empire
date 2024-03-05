from typing import TypedDict, Literal

# Types

MaxUnpool3dDimensionParam = int | tuple[int, int, int]

MaxUnpool3dDimensionParamsKeyof = Literal["kernel_size", "stride", "padding"]


# Main

class MaxUnpool3dDimensionParams(TypedDict):
    kernel_size: MaxUnpool3dDimensionParam
    stride: MaxUnpool3dDimensionParam
    padding: MaxUnpool3dDimensionParam
