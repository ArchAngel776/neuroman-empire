from .params import ReflectionPadBoundedParams
from .options import ReflectionPadBoundedOptions


# Main

class ReflectionPaddingBoundedExtension:
    @staticmethod
    def default_params() -> ReflectionPadBoundedParams: ...

    @staticmethod
    def default_options() -> ReflectionPadBoundedOptions: ...
