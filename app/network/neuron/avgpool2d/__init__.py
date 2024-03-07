from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType
from app.network.neuron.avgpool2d.params import AvgPool2dParams
from app.network.neuron.avgpool2d.options import AvgPool2dOptions


# Main

class AveragePooling2d(Neuron):
    @staticmethod
    def type():
        return NeuronType.AVGPOOL2D

    @staticmethod
    def title():
        return "Average Pooling 2D"

    @staticmethod
    def default_params():
        return AvgPool2dParams(
            ceil_mode=True,
            kernel_size=(1, 1),
            stride=(1, 1),
            padding=(0, 0),
            count_include_pad=True,
            divisor_override=1
        )

    @staticmethod
    def default_options():
        return AvgPool2dOptions(
            square=False,
            divisor_enabled=False
        )
