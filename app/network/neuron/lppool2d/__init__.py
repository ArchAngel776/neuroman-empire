from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType
from app.network.neuron.lppool2d.params import LPPool2dParams
from app.network.neuron.lppool2d.options import LPPool2dOptions


# Main

class LocalPooling2d(Neuron):
    @staticmethod
    def type():
        return NeuronType.LPPOOL2D

    @staticmethod
    def title():
        return "Local Pooling 2D"

    @staticmethod
    def default_params():
        return LPPool2dParams(
            power=2,
            ceil_mode=True,
            kernel_size=(1, 1),
            stride=(1, 1)
        )

    @staticmethod
    def default_options():
        return LPPool2dOptions(
            square=False
        )
