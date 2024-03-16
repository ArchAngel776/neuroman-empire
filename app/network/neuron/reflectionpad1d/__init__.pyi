from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import ReflectionPad1dParams
from .options import ReflectionPad1dOptions


# Main

class ReflectionPadding1d(Neuron[ReflectionPad1dParams, ReflectionPad1dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> ReflectionPad1dParams: ...

    @staticmethod
    def default_options() -> ReflectionPad1dOptions: ...
