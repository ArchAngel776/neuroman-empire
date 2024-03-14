from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType
from app.network.neuron.adaptiveavgpool1d.params import AdaptiveAvgPool1dParams
from app.network.neuron.adaptiveavgpool1d.options import AdaptiveAvgPool1dOptions


# Main

class AdaptiveAveragePooling1d(Neuron):
    @staticmethod
    def type():
        return NeuronType.ADAPTIVEAVGPOOL1D

    @staticmethod
    def title():
        return "Adaptive Average Pooling 1D"

    @staticmethod
    def default_params():
        return AdaptiveAvgPool1dParams(
            output_size=1
        )

    @staticmethod
    def default_options():
        return AdaptiveAvgPool1dOptions()
