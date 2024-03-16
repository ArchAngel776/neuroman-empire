from .params import ReplicationPadBoundedParams
from .options import ReplicationPadBoundedOptions


# Main

class ReplicationPaddingBoundedExtension:
    @staticmethod
    def default_params() -> ReplicationPadBoundedParams: ...

    @staticmethod
    def default_options() -> ReplicationPadBoundedOptions: ...
