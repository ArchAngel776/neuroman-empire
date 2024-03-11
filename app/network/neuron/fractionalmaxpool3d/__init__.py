from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType
from app.network.neuron.fractionalmaxpool3d.params import FractionalMaxPool3dParams
from app.network.neuron.fractionalmaxpool3d.options import FractionalMaxPool3dOptions
from app.network.neuron.fractionalmaxpool3d.dimension.options.output import Output


# Main

class FractionalMaxPooling3d(Neuron):
    @staticmethod
    def type():
        return NeuronType.FRACTIONALMAXPOOL3D

    @staticmethod
    def title():
        return "Fractional Max Pooling 3D"

    @staticmethod
    def default_params():
        return FractionalMaxPool3dParams(
            kernel_size=(1, 1, 1),
            output_size=(1, 1, 1),
            output_ratio=(.5, .5, .5),
            return_indices=False
        )

    @staticmethod
    def default_options():
        return FractionalMaxPool3dOptions(
            cube=False,
            output=Output.SIZE
        )
