from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType
from app.network.neuron.maxpool3d.params import MaxPool3dParams
from app.network.neuron.maxpool3d.options import MaxPool3dOptions


# Main

class MaxPooling3d(Neuron):
    @staticmethod
    def type():
        return NeuronType.MAXPOOL3D

    @staticmethod
    def title():
        return "Max Pooling 3D"

    @staticmethod
    def default_params():
        return MaxPool3dParams(
            ceil_mode=True,
            kernel_size=(1, 1, 1),
            stride=(1, 1, 1),
            padding=(0, 0, 0),
            dilation=(1, 1, 1),
            return_indices=False
        )

    @staticmethod
    def default_options():
        return MaxPool3dOptions(
            cube=False
        )
