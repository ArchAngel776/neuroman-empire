from uuid import UUID

from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType
from app.network.neuron.maxunpool3d.params import MaxUnpool3dParams
from app.network.neuron.maxunpool3d.options import MaxUnpool3dOptions


# Main

class MaxUnpooling1d(Neuron):
    @staticmethod
    def type():
        return NeuronType.MAXUNPOOL3D

    @staticmethod
    def title():
        return "Max Unpooling 3D"

    @staticmethod
    def default_params():
        return MaxUnpool3dParams(
            kernel_size=(1, 1, 1),
            stride=(1, 1, 1),
            padding=(0, 0, 0)
        )

    @staticmethod
    def default_options():
        return MaxUnpool3dOptions(
            pooling=UUID(),
            cube=False
        )
