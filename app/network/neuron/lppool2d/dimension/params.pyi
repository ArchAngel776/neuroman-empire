from typing import TypedDict, Literal

# Types

LPPool2dDimensionParam = int | tuple[int, int]

LPPool2dDimensionParamsKeyof = Literal["kernel_size", "stride"]


# Main

class LPPool2dDimensionParams(TypedDict):
    kernel_size: LPPool2dDimensionParam
    stride: LPPool2dDimensionParam
