from typing import TypedDict, Literal

# Types

ConvTranspose2dDimensionParam = int | tuple[int, int]

ConvTranspose2dDimensionParamsKeyof = Literal["kernel_size", "stride", "padding", "dilation", "output_padding"]


# Main

class ConvTranspose2dDimensionParams(TypedDict):
    kernel_size: ConvTranspose2dDimensionParam
    stride: ConvTranspose2dDimensionParam
    padding: ConvTranspose2dDimensionParam
    dilation: ConvTranspose2dDimensionParam
    output_padding: ConvTranspose2dDimensionParam
