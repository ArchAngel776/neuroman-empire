from typing import TypedDict, Literal

# Types

FractionalMaxPool2dDimensionOutputSizeParam = int | tuple[int, int]

FractionalMaxPool2dDimensionOutputSizeParamsKeyof = Literal["output_size"]


# Main

class FractionalMaxPool2dDimensionOutputSizeParams(TypedDict):
    output_size: FractionalMaxPool2dDimensionOutputSizeParam
