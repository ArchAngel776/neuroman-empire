from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType
from app.network.neuron.adaptivemaxpool1d.params import AdaptiveMaxPool1dParams
from app.network.neuron.adaptivemaxpool1d.options import AdaptiveMaxPool1dOptions


# Main

class AdaptiveMaxPooling1d(Neuron):
    @staticmethod
    def type():
        return NeuronType.ADAPTIVEMAXPOOL1D

    @staticmethod
    def title():
        return "Adaptive Max Pooling 1D"

    @staticmethod
    def default_params():
        return AdaptiveMaxPool1dParams(
            output_size=1,
            return_indices=False
        )

    @staticmethod
    def default_options():
        return AdaptiveMaxPool1dOptions()
