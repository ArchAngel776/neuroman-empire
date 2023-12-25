from typing import TypedDict, Literal

# Types

ConvTranspose3dDimensionParam = int | tuple[int, int, int]

ConvTranspose3dDimensionParamsKeyof = Literal["kernel_size", "stride", "padding", "dilation", "output_padding"]


# Main

class ConvTranspose3dDimensionParams(TypedDict):
    kernel_size: ConvTranspose3dDimensionParam
    stride: ConvTranspose3dDimensionParam
    padding: ConvTranspose3dDimensionParam
    dilation: ConvTranspose3dDimensionParam
    output_padding: ConvTranspose3dDimensionParam
