from app.network.neuron.fractionalmaxpool3d.dimension.params.output.size import \
    FractionalMaxPool3dDimensionOutputSizeParams
from app.network.neuron.fractionalmaxpool3d.dimension.params.output.ratio import \
    FractionalMaxPool3dDimensionOutputRatioParams


# Main

class FractionalMaxPool3dDimensionParams(
    FractionalMaxPool3dDimensionOutputSizeParams,
    FractionalMaxPool3dDimensionOutputRatioParams
):
    pass
