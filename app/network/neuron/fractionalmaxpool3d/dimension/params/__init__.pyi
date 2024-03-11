from typing import Literal

from .output.size import FractionalMaxPool3dDimensionOutputSizeParams
from .output.ratio import FractionalMaxPool3dDimensionOutputRatioParams

# Types

FractionalMaxPool3dDimensionParam = int | tuple[int, int, int]

FractionalMaxPool3dDimensionParamsKeyof = Literal["kernel_size"]


# Main

class FractionalMaxPool3dDimensionParams(
    FractionalMaxPool3dDimensionOutputSizeParams,
    FractionalMaxPool3dDimensionOutputRatioParams
):
    kernel_size: FractionalMaxPool3dDimensionParam
