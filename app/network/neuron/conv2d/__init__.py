from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType
from app.network.neuron.conv2d.options import Conv2dOptions
from app.network.neuron.conv2d.params import Conv2dParams


# Main

class Convolution2d(Neuron):
    @staticmethod
    def type():
        return NeuronType.CONV2D

    @staticmethod
    def title():
        return "Convolution 2D"

    @staticmethod
    def default_params():
        return Conv2dParams(
            in_channels=1,
            out_channels=1,
            kernel_size=(1, 1),
            stride=(1, 1),
            padding=(0, 0),
            dilation=(1, 1),
            groups=1,
            bias=True
        )

    @staticmethod
    def default_options():
        return Conv2dOptions(
            square=False
        )
