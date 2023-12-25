from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType
from app.network.neuron.maxpool1d.params import MaxPool1dParams
from app.network.neuron.maxpool1d.options import MaxPool1dOptions


# Main

class MaxPooling1d(Neuron):
    @staticmethod
    def type():
        return NeuronType.MAXPOOL1D

    @staticmethod
    def title():
        return "Max Pooling 1D"

    @staticmethod
    def default_params():
        return MaxPool1dParams(
            ceil_mode=True,
            kernel_size=1,
            stride=1,
            padding=0,
            dilation=1,
            return_indices=False
        )

    @staticmethod
    def default_options():
        return MaxPool1dOptions()
