from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import ReplicationPad1dParams
from .options import ReplicationPad1dOptions


# Main

class ReplicationPadding1d(Neuron[ReplicationPad1dParams, ReplicationPad1dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> ReplicationPad1dParams: ...

    @staticmethod
    def default_options() -> ReplicationPad1dOptions: ...
