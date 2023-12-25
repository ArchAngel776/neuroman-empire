from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType
from app.network.neuron.maxpool2d.params import MaxPool2dParams
from app.network.neuron.maxpool2d.options import MaxPool2dOptions


# Main

class MaxPooling2d(Neuron):
    @staticmethod
    def type():
        return NeuronType.MAXPOOL2D

    @staticmethod
    def title():
        return "Max Pooling 2D"

    @staticmethod
    def default_params():
        return MaxPool2dParams(
            ceil_mode=True,
            kernel_size=(1, 1),
            stride=(1, 1),
            padding=(0, 0),
            dilation=(1, 1),
            return_indices=False
        )

    @staticmethod
    def default_options():
        return MaxPool2dOptions(
            square=False
        )
