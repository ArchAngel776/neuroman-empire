from typing import Literal

from .output.size import FractionalMaxPool2dDimensionOutputSizeParams
from .output.ratio import FractionalMaxPool2dDimensionOutputRatioParams

# Types

FractionalMaxPool2dDimensionParam = int | tuple[int, int]

FractionalMaxPool2dDimensionParamsKeyof = Literal["kernel_size"]


# Main

class FractionalMaxPool2dDimensionParams(
    FractionalMaxPool2dDimensionOutputSizeParams,
    FractionalMaxPool2dDimensionOutputRatioParams
):
    kernel_size: FractionalMaxPool2dDimensionParam
