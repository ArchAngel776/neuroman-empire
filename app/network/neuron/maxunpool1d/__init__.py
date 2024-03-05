from uuid import UUID

from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType
from app.network.neuron.maxunpool1d.params import MaxUnpool1dParams
from app.network.neuron.maxunpool1d.options import MaxUnpool1dOptions


# Main

class MaxUnpooling1d(Neuron):
    @staticmethod
    def type():
        return NeuronType.MAXPOOL1D

    @staticmethod
    def title():
        return "Max Unpooling 1D"

    @staticmethod
    def default_params():
        return MaxUnpool1dParams(
            kernel_size=1,
            stride=1,
            padding=0
        )

    @staticmethod
    def default_options():
        return MaxUnpool1dOptions(
            pooling=UUID()
        )
