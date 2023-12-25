from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType
from app.network.neuron.unfold.params import UnfoldParams
from app.network.neuron.unfold.options import UnfoldOptions


# Main

class Unfold(Neuron):
    @staticmethod
    def type():
        return NeuronType.UNFOLD

    @staticmethod
    def title():
        return "Unfold"

    @staticmethod
    def default_params():
        return UnfoldParams(
            kernel_size=[1, 1, 1],
            dilation=[1, 1, 1],
            padding=[0, 0, 0],
            stride=[1, 1, 1]
        )

    @staticmethod
    def default_options():
        return UnfoldOptions()
