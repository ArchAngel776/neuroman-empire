from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import ReplicationPad3dParams
from .options import ReplicationPad3dOptions


# Main

class ReplicationPadding3d(Neuron):
    @staticmethod
    def type():
        return NeuronType.REPLICATIONPAD3D

    @staticmethod
    def title():
        return "Replication Padding 3D"

    @staticmethod
    def default_params():
        return ReplicationPad3dParams(
            padding=(0, 0, 0, 0, 0, 0)
        )

    @staticmethod
    def default_options():
        return ReplicationPad3dOptions(
            bounded=False
        )
