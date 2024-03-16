from .params import ConstantPadBoundedParams
from .options import ConstantPadBoundedOptions


# Main

class ConstantPaddingBoundedExtension:
    @staticmethod
    def default_params() -> ConstantPadBoundedParams: ...

    @staticmethod
    def default_options() -> ConstantPadBoundedOptions: ...
