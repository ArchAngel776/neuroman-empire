from app.network.extension.reflectionpad.bounded.params import ReflectionPadBoundedParams
from app.network.extension.reflectionpad.bounded.options import ReflectionPadBoundedOptions


# Main

class ReflectionPaddingBoundedExtension:
    @staticmethod
    def default_params():
        return ReflectionPadBoundedParams(
            padding=0
        )

    @staticmethod
    def default_options():
        return ReflectionPadBoundedOptions()
