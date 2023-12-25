from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType
from app.network.neuron.convtranspose1d.params import ConvTranspose1dParams
from app.network.neuron.convtranspose1d.options import ConvTranspose1dOptions


# Main

class TransposedConvolution1d(Neuron):
    @staticmethod
    def type():
        return NeuronType.CONVTRANSPOSE1D

    @staticmethod
    def title():
        return "Transposed Convolution 1D"

    @staticmethod
    def default_params():
        return ConvTranspose1dParams(
            in_channels=1,
            out_channels=1,
            kernel_size=1,
            stride=1,
            padding=0,
            dilation=1,
            output_padding=0,
            groups=1,
            bias=True
        )

    @staticmethod
    def default_options():
        return ConvTranspose1dOptions()
