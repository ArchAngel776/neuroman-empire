from typing import Literal

from .output.size import FractionalMaxPoolSingleDimensionOutputSizeOptions
from .output.ratio import FractionalMaxPoolSingleDimensionOutputRatioOptions
from .output import Output

# Types

FractionalMaxPoolSingleDimensionOptionsKeyof = Literal["output"]


# Main

class FractionalMaxPoolSingleDimensionOptions(
    FractionalMaxPoolSingleDimensionOutputSizeOptions,
    FractionalMaxPoolSingleDimensionOutputRatioOptions
):
    output: Output
