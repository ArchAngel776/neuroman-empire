from app.network.extension.zeropad.bounded.params import ZeroPadBoundedParams
from app.network.extension.zeropad.bounded.options import ZeroPadBoundedOptions


# Main

class ZeroPaddingBoundedExtension:
    @staticmethod
    def default_params():
        return ZeroPadBoundedParams(
            padding=0
        )

    @staticmethod
    def default_options():
        return ZeroPadBoundedOptions()
