from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType
from app.network.neuron.convtranspose3d.params import ConvTranspose3dParams
from app.network.neuron.convtranspose3d.options import ConvTranspose3dOptions


# Main

class TransposedConvolution3d(Neuron):
    @staticmethod
    def type():
        return NeuronType.CONVTRANSPOSE3D

    @staticmethod
    def title():
        return "Transposed Convolution 3D"

    @staticmethod
    def default_params():
        return ConvTranspose3dParams(
            in_channels=1,
            out_channels=1,
            kernel_size=(1, 1, 1),
            stride=(1, 1, 1),
            padding=(0, 0, 0),
            dilation=(1, 1, 1),
            output_padding=(0, 0, 0),
            groups=1,
            bias=True
        )

    @staticmethod
    def default_options():
        return ConvTranspose3dOptions(
            cube=False
        )
