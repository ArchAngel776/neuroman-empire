from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType
from app.network.neuron.adaptivemaxpool2d.params import AdaptiveMaxPool2dParams
from app.network.neuron.adaptivemaxpool2d.options import AdaptiveMaxPool2dOptions


# Main

class AdaptiveMaxPooling2d(Neuron):
    @staticmethod
    def type():
        return NeuronType.ADAPTIVEMAXPOOL2D

    @staticmethod
    def title():
        return "Adaptive Max Pooling 2D"

    @staticmethod
    def default_params():
        return AdaptiveMaxPool2dParams(
            output_size=(1, 1),
            return_indices=False
        )

    @staticmethod
    def default_options():
        return AdaptiveMaxPool2dOptions(
            square=False
        )
