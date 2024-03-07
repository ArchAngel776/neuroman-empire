from uuid import UUID

from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType
from app.network.neuron.maxunpool2d.params import MaxUnpool2dParams
from app.network.neuron.maxunpool2d.options import MaxUnpool2dOptions


# Main

class MaxUnpooling2d(Neuron):
    @staticmethod
    def type():
        return NeuronType.MAXUNPOOL2D

    @staticmethod
    def title():
        return "Max Unpooling 2D"

    @staticmethod
    def default_params():
        return MaxUnpool2dParams(
            kernel_size=(1, 1),
            stride=(1, 1),
            padding=(0, 0)
        )

    @staticmethod
    def default_options():
        return MaxUnpool2dOptions(
            pooling=UUID(),
            square=False
        )
