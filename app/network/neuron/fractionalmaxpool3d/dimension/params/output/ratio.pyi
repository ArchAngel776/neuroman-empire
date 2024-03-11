from typing import TypedDict, Literal

# Types

FractionalMaxPool3dDimensionOutputRatioParam = float | tuple[float, float, float]

FractionalMaxPool3dDimensionOutputRatioParamsKeyof = Literal["output_ratio"]


# Main

class FractionalMaxPool3dDimensionOutputRatioParams(TypedDict):
    output_ratio: FractionalMaxPool3dDimensionOutputRatioParam
