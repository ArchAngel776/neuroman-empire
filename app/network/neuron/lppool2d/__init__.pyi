from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import LPPool2dParams
from .options import LPPool2dOptions


# Main

class LocalPooling2d(Neuron[LPPool2dParams, LPPool2dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> LPPool2dParams: ...

    @staticmethod
    def default_options() -> LPPool2dOptions: ...
