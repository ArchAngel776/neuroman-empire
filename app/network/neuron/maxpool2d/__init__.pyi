from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import MaxPool2dParams
from .options import MaxPool2dOptions


# Main

class MaxPooling2d(Neuron[MaxPool2dParams, MaxPool2dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> MaxPool2dParams: ...

    @staticmethod
    def default_options() -> MaxPool2dOptions: ...
