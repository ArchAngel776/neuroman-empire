from app.network.extension.fractionalmaxpool.single.params.output.size import \
    FractionalMaxPoolSingleDimensionOutputSizeParams
from app.network.extension.fractionalmaxpool.single.params.output.ratio import \
    FractionalMaxPoolSingleDimensionOutputRatioParams


# Main

class FractionalMaxPoolSingleDimensionParams(
    FractionalMaxPoolSingleDimensionOutputSizeParams,
    FractionalMaxPoolSingleDimensionOutputRatioParams
):
    pass
