from typing import TypedDict, Literal

# Types

ConvTranspose1dDimensionParam = int

ConvTranspose1dDimensionParamsKeyof = Literal["kernel_size", "stride", "padding", "dilation", "output_padding"]


# Main

class ConvTranspose1dDimensionParams(TypedDict):
    kernel_size: ConvTranspose1dDimensionParam
    stride: ConvTranspose1dDimensionParam
    padding: ConvTranspose1dDimensionParam
    dilation: ConvTranspose1dDimensionParam
    output_padding: ConvTranspose1dDimensionParam
