from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType
from app.network.neuron.lppool1d.params import LPPool1dParams
from app.network.neuron.lppool1d.options import LPPool1dOptions


# Main

class LocalPooling1d(Neuron):
    @staticmethod
    def type():
        return NeuronType.LPPOOL1D

    @staticmethod
    def title():
        return "Local Pooling 1D"

    @staticmethod
    def default_params():
        return LPPool1dParams(
            power=2,
            ceil_mode=True,
            kernel_size=1,
            stride=1
        )

    @staticmethod
    def default_options():
        return LPPool1dOptions()
