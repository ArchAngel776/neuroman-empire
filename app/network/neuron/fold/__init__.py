from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType
from app.network.neuron.fold.params import FoldParams
from app.network.neuron.fold.options import FoldOptions


# Main

class Fold(Neuron):
    @staticmethod
    def type():
        return NeuronType.FOLD

    @staticmethod
    def title():
        return "Fold"

    @staticmethod
    def default_params():
        return FoldParams(
            output_size=[1],
            kernel_size=[1],
            dilation=[1],
            padding=[0],
            stride=[1]
        )

    @staticmethod
    def default_options():
        return FoldOptions()
