from .params import CircularPadBoundedParams
from .options import CircularPadBoundedOptions


# Main

class CircularPaddingBoundedExtension:
    @staticmethod
    def default_params() -> CircularPadBoundedParams: ...

    @staticmethod
    def default_options() -> CircularPadBoundedOptions: ...
