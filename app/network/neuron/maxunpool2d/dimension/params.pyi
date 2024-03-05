from typing import TypedDict, Literal

# Types

MaxUnpool2dDimensionParam = int | tuple[int, int]

MaxUnpool2dDimensionParamsKeyof = Literal["kernel_size", "stride", "padding"]


# Main

class MaxUnpool2dDimensionParams(TypedDict):
    kernel_size: MaxUnpool2dDimensionParam
    stride: MaxUnpool2dDimensionParam
    padding: MaxUnpool2dDimensionParam
