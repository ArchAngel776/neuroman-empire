from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import ReplicationPad2dParams
from .options import ReplicationPad2dOptions


# Main

class ReplicationPadding2d(Neuron[ReplicationPad2dParams, ReplicationPad2dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> ReplicationPad2dParams: ...

    @staticmethod
    def default_options() -> ReplicationPad2dOptions: ...
