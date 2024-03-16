from app.network.extension.replicationpad.bounded.params import ReplicationPadBoundedParams
from app.network.extension.replicationpad.bounded.options import ReplicationPadBoundedOptions


# Main

class ReplicationPaddingBoundedExtension:
    @staticmethod
    def default_params():
        return ReplicationPadBoundedParams(
            padding=0
        )

    @staticmethod
    def default_options():
        return ReplicationPadBoundedOptions()
