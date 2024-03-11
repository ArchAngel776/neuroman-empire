from app.network.extension.fractionalmaxpool.single.options.output.size import \
    FractionalMaxPoolSingleDimensionOutputSizeOptions
from app.network.extension.fractionalmaxpool.single.options.output.ratio import \
    FractionalMaxPoolSingleDimensionOutputRatioOptions


# Main

class FractionalMaxPoolSingleDimensionOptions(
    FractionalMaxPoolSingleDimensionOutputSizeOptions,
    FractionalMaxPoolSingleDimensionOutputRatioOptions
):
    pass
