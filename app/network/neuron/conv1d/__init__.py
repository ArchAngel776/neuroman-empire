from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType
from app.network.neuron.conv1d.params import Conv1dParams
from app.network.neuron.conv1d.options import Conv1dOptions


# Main

class Convolution1d(Neuron):
    @staticmethod
    def type():
        return NeuronType.CONV1D

    @staticmethod
    def title():
        return "Convolution 1D"

    @staticmethod
    def default_params():
        return Conv1dParams(
            in_channels=1,
            out_channels=1,
            kernel_size=1,
            stride=1,
            padding=0,
            dilation=1,
            groups=1,
            bias=True
        )

    @staticmethod
    def default_options():
        return Conv1dOptions()
