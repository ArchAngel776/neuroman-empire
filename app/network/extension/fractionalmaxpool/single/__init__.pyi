from .params import FractionalMaxPoolSingleDimensionParams
from .options import FractionalMaxPoolSingleDimensionOptions


# Main

class FractionalMaxPoolingSingleExtension:
    @staticmethod
    def default_params() -> FractionalMaxPoolSingleDimensionParams: ...

    @staticmethod
    def default_options() -> FractionalMaxPoolSingleDimensionOptions: ...
