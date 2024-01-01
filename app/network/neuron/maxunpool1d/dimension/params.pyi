from typing import TypedDict, Literal

# Types

MaxUnpool1dDimensionParam = int

MaxUnpool1dDimensionParamsKeyof = Literal["kernel_size", "stride", "padding"]


# Main

class MaxUnpool1dDimensionParams(TypedDict):
    kernel_size: MaxUnpool1dDimensionParam
    stride: MaxUnpool1dDimensionParam
    padding: MaxUnpool1dDimensionParam
