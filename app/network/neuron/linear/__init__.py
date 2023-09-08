from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType
from app.network.neuron.linear.params import LinearParams
from app.network.neuron.linear.options import LinearOptions


# Main

class Linear(Neuron):
    @staticmethod
    def type():
        return NeuronType.LINEAR

    @staticmethod
    def title():
        return "Linear"

    @staticmethod
    def default_params():
        return LinearParams(
            in_features=1,
            out_features=1,
            bias=True
        )

    @staticmethod
    def default_options():
        return LinearOptions()
