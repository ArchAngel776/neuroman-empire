from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import AdaptiveAvgPool2dParams
from .options import AdaptiveAvgPool2dOptions


# Main

class AdaptiveAveragePooling2d(Neuron[AdaptiveAvgPool2dParams, AdaptiveAvgPool2dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> AdaptiveAvgPool2dParams: ...

    @staticmethod
    def default_options() -> AdaptiveAvgPool2dOptions: ...
