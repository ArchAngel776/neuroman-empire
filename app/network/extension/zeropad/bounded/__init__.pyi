from .params import ZeroPadBoundedParams
from .options import ZeroPadBoundedOptions


# Main

class ZeroPaddingBoundedExtension:
    @staticmethod
    def default_params() -> ZeroPadBoundedParams: ...

    @staticmethod
    def default_options() -> ZeroPadBoundedOptions: ...
