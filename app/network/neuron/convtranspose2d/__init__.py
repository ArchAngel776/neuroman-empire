from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType
from app.network.neuron.convtranspose2d.options import ConvTranspose2dOptions
from app.network.neuron.convtranspose2d.params import ConvTranspose2dParams


# Main

class TransposedConvolution2d(Neuron):
    @staticmethod
    def type():
        return NeuronType.CONVTRANSPOSE2D

    @staticmethod
    def title():
        return "Transposed Convolution 2D"

    @staticmethod
    def default_params():
        return ConvTranspose2dParams(
            in_channels=1,
            out_channels=1,
            kernel_size=(1, 1),
            stride=(1, 1),
            padding=(0, 0),
            dilation=(1, 1),
            output_padding=(0, 0),
            groups=1,
            bias=True
        )

    @staticmethod
    def default_options():
        return ConvTranspose2dOptions(
            square=False
        )
