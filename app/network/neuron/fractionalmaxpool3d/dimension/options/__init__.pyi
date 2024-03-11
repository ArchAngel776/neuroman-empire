from typing import Literal

from .output.size import FractionalMaxPool3dDimensionOutputSizeOptions
from .output.ratio import FractionalMaxPool3dDimensionOutputRatioOptions
from .output import Output

# Types

FractionalMaxPool3dDimensionOptionsKeyof = Literal["output"]


# Main

class FractionalMaxPool3dDimensionOptions(
    FractionalMaxPool3dDimensionOutputSizeOptions,
    FractionalMaxPool3dDimensionOutputRatioOptions
):
    output: Output
