from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType
from app.network.neuron.adaptiveavgpool2d.params import AdaptiveAvgPool2dParams
from app.network.neuron.adaptiveavgpool2d.options import AdaptiveAvgPool2dOptions


# Main

class AdaptiveAveragePooling2d(Neuron):
    @staticmethod
    def type():
        return NeuronType.ADAPTIVEAVGPOOL2D

    @staticmethod
    def title():
        return "Adaptive Average Pooling 2D"

    @staticmethod
    def default_params():
        return AdaptiveAvgPool2dParams(
            output_size=(1, 1)
        )

    @staticmethod
    def default_options():
        return AdaptiveAvgPool2dOptions(
            square=False,
            output_enabled=(True, True)
        )
