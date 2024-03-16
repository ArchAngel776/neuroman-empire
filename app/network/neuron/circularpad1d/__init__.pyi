from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import CircularPad1dParams
from .options import CircularPad1dOptions


# Main

class CircularPadding1d(Neuron[CircularPad1dParams, CircularPad1dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> CircularPad1dParams: ...

    @staticmethod
    def default_options() -> CircularPad1dOptions: ...
