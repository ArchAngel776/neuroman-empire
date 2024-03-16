from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import ZeroPad1dParams
from .options import ZeroPad1dOptions


# Main

class ZeroPadding1d(Neuron[ZeroPad1dParams, ZeroPad1dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> ZeroPad1dParams: ...

    @staticmethod
    def default_options() -> ZeroPad1dOptions: ...
