from app.network.extension.constantpad.bounded.params import ConstantPadBoundedParams
from app.network.extension.constantpad.bounded.options import ConstantPadBoundedOptions


# Main

class ConstantPaddingBoundedExtension:
    @staticmethod
    def default_params():
        return ConstantPadBoundedParams(
            padding=0
        )

    @staticmethod
    def default_options():
        return ConstantPadBoundedOptions()
