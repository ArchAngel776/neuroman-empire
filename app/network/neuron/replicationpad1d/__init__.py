from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import ReplicationPad1dParams
from .options import ReplicationPad1dOptions


# Main

class ReplicationPadding1d(Neuron):
    @staticmethod
    def type():
        return NeuronType.REPLICATIONPAD1D

    @staticmethod
    def title():
        return "Replication Padding 1D"

    @staticmethod
    def default_params():
        return ReplicationPad1dParams(
            padding=(0, 0)
        )

    @staticmethod
    def default_options():
        return ReplicationPad1dOptions(
            bounded=False
        )
