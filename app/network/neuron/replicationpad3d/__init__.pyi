from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import ReplicationPad3dParams
from .options import ReplicationPad3dOptions


# Main

class ReplicationPadding3d(Neuron[ReplicationPad3dParams, ReplicationPad3dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> ReplicationPad3dParams: ...

    @staticmethod
    def default_options() -> ReplicationPad3dOptions: ...
