from typing import TypedDict, Literal

# Types

FractionalMaxPool3dDimensionOutputSizeParam = int | tuple[int, int, int]

FractionalMaxPool3dDimensionOutputSizeParamsKeyof = Literal["output_size"]


# Main

class FractionalMaxPool3dDimensionOutputSizeParams(TypedDict):
    output_size: FractionalMaxPool3dDimensionOutputSizeParam
