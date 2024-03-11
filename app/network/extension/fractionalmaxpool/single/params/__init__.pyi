from typing import Literal

from .output.size import FractionalMaxPoolSingleDimensionOutputSizeParams
from .output.ratio import FractionalMaxPoolSingleDimensionOutputRatioParams

# Types

FractionalMaxPoolSingleDimensionParam = int

FractionalMaxPoolSingleDimensionParamsKeyof = Literal["kernel_size"]


# Main

class FractionalMaxPoolSingleDimensionParams(
    FractionalMaxPoolSingleDimensionOutputSizeParams,
    FractionalMaxPoolSingleDimensionOutputRatioParams
):
    kernel_size: FractionalMaxPoolSingleDimensionParam
