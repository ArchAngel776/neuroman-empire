from app.network.extension.fractionalmaxpool.single.options.output import Output
from app.network.extension.fractionalmaxpool.single.params import FractionalMaxPoolSingleDimensionParams
from app.network.extension.fractionalmaxpool.single.options import FractionalMaxPoolSingleDimensionOptions


# Main

class FractionalMaxPoolingSingleExtension:
    @staticmethod
    def default_params():
        return FractionalMaxPoolSingleDimensionParams(
            kernel_size=1,
            output_size=1,
            output_ratio=.5
        )

    @staticmethod
    def default_options():
        return FractionalMaxPoolSingleDimensionOptions(
            output=Output.SIZE
        )
