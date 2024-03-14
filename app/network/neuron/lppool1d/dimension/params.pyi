from typing import TypedDict, Literal

# Types

LPPool1dDimensionParam = int

LPPool1dDimensionParamsKeyof = Literal["kernel_size", "stride"]


# Main

class LPPool1dDimensionParams(TypedDict):
    kernel_size: LPPool1dDimensionParam
    stride: LPPool1dDimensionParam
