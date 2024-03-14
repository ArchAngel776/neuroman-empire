from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import LPPool1dParams
from .options import LPPool1dOptions


# Main

class LocalPooling1d(Neuron[LPPool1dParams, LPPool1dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> LPPool1dParams: ...

    @staticmethod
    def default_options() -> LPPool1dOptions: ...
