from app.network.neuron.fractionalmaxpool2d.dimension.options.output.size import \
    FractionalMaxPool2dDimensionOutputSizeOptions
from app.network.neuron.fractionalmaxpool2d.dimension.options.output.ratio import \
    FractionalMaxPool2dDimensionOutputRatioOptions


# Main

class FractionalMaxPool2dDimensionOptions(
    FractionalMaxPool2dDimensionOutputSizeOptions,
    FractionalMaxPool2dDimensionOutputRatioOptions
):
    pass
