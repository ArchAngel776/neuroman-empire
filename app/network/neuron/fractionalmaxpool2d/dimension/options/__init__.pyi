from typing import Literal

from .output.size import FractionalMaxPool2dDimensionOutputSizeOptions
from .output.ratio import FractionalMaxPool2dDimensionOutputRatioOptions
from .output import Output

# Types

FractionalMaxPool2dDimensionOptionsKeyof = Literal["output"]


# Main

class FractionalMaxPool2dDimensionOptions(
    FractionalMaxPool2dDimensionOutputSizeOptions,
    FractionalMaxPool2dDimensionOutputRatioOptions
):
    output: Output
