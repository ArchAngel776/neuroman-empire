from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType
from app.network.neuron.conv3d.params import Conv3dParams
from app.network.neuron.conv3d.options import Conv3dOptions


# Main

class Convolution3d(Neuron):
    @staticmethod
    def type():
        return NeuronType.CONV3D

    @staticmethod
    def title():
        return "Convolution 3D"

    @staticmethod
    def default_params():
        return Conv3dParams(
            in_channels=1,
            out_channels=1,
            kernel_size=(1, 1, 1),
            stride=(1, 1, 1),
            padding=(0, 0, 0),
            dilation=(1, 1, 1),
            groups=1,
            bias=True
        )

    @staticmethod
    def default_options():
        return Conv3dOptions(
            cube=False
        )
