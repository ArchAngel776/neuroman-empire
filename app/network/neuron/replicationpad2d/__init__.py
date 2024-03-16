from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import ReplicationPad2dParams
from .options import ReplicationPad2dOptions


# Main

class ReplicationPadding2d(Neuron):
    @staticmethod
    def type():
        return NeuronType.REPLICATIONPAD2D

    @staticmethod
    def title():
        return "Replication Padding 2D"

    @staticmethod
    def default_params():
        return ReplicationPad2dParams(
            padding=(0, 0, 0, 0)
        )

    @staticmethod
    def default_options():
        return ReplicationPad2dOptions(
            bounded=False
        )
