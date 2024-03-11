from typing import TypedDict, Literal

# Types

FractionalMaxPool2dDimensionOutputRatioParam = float | tuple[float, float]

FractionalMaxPool2dDimensionOutputRatioParamsKeyof = Literal["output_ratio"]


# Main

class FractionalMaxPool2dDimensionOutputRatioParams(TypedDict):
    output_ratio: FractionalMaxPool2dDimensionOutputRatioParam
