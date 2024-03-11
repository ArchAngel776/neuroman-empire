from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType
from app.network.neuron.fractionalmaxpool2d.params import FractionalMaxPool2dParams
from app.network.neuron.fractionalmaxpool2d.options import FractionalMaxPool2dOptions
from app.network.neuron.fractionalmaxpool2d.dimension.options.output import Output


# Main

class FractionalMaxPooling2d(Neuron):
    @staticmethod
    def type():
        return NeuronType.FRACTIONALMAXPOOL2D

    @staticmethod
    def title():
        return "Fractional Max Pooling 2D"

    @staticmethod
    def default_params():
        return FractionalMaxPool2dParams(
            kernel_size=(1, 1),
            output_size=(1, 1),
            output_ratio=(.5, .5),
            return_indices=False
        )

    @staticmethod
    def default_options():
        return FractionalMaxPool2dOptions(
            square=False,
            output=Output.SIZE
        )
