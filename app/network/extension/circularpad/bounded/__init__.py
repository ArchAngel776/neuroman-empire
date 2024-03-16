from app.network.extension.circularpad.bounded.params import CircularPadBoundedParams
from app.network.extension.circularpad.bounded.options import CircularPadBoundedOptions


# Main

class CircularPaddingBoundedExtension:
    @staticmethod
    def default_params():
        return CircularPadBoundedParams(
            padding=0
        )

    @staticmethod
    def default_options():
        return CircularPadBoundedOptions()
