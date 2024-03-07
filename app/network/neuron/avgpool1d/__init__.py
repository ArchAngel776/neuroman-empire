from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType
from app.network.neuron.avgpool1d.params import AvgPool1dParams
from app.network.neuron.avgpool1d.options import AvgPool1dOptions


# Main

class AveragePooling1d(Neuron):
    @staticmethod
    def type():
        return NeuronType.AVGPOOL1D

    @staticmethod
    def title():
        return "Average Pooling 1D"

    @staticmethod
    def default_params():
        return AvgPool1dParams(
            ceil_mode=True,
            kernel_size=1,
            stride=1,
            padding=0,
            count_include_pad=True
        )

    @staticmethod
    def default_options():
        return AvgPool1dOptions()
