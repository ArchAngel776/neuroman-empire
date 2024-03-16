from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import ReflectionPad3dParams
from .options import ReflectionPad3dOptions


# Main

class ReflectionPadding3d(Neuron[ReflectionPad3dParams, ReflectionPad3dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> ReflectionPad3dParams: ...

    @staticmethod
    def default_options() -> ReflectionPad3dOptions: ...
