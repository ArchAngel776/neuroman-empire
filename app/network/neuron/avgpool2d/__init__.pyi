from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import AvgPool2dParams
from .options import AvgPool2dOptions


# Main

class AveragePooling2d(Neuron[AvgPool2dParams, AvgPool2dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> AvgPool2dParams: ...

    @staticmethod
    def default_options() -> AvgPool2dOptions: ...
