from app.network.neuron.fractionalmaxpool2d.dimension.params.output.size import \
    FractionalMaxPool2dDimensionOutputSizeParams
from app.network.neuron.fractionalmaxpool2d.dimension.params.output.ratio import \
    FractionalMaxPool2dDimensionOutputRatioParams


# Main

class FractionalMaxPool2dDimensionParams(
    FractionalMaxPool2dDimensionOutputSizeParams,
    FractionalMaxPool2dDimensionOutputRatioParams
):
    pass
