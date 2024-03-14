from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import AdaptiveMaxPool2dParams
from .options import AdaptiveMaxPool2dOptions


# Main

class AdaptiveMaxPooling2d(Neuron[AdaptiveMaxPool2dParams, AdaptiveMaxPool2dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> AdaptiveMaxPool2dParams: ...

    @staticmethod
    def default_options() -> AdaptiveMaxPool2dOptions: ...
