from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import CircularPad3dParams
from .options import CircularPad3dOptions


# Main

class CircularPadding3d(Neuron[CircularPad3dParams, CircularPad3dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> CircularPad3dParams: ...

    @staticmethod
    def default_options() -> CircularPad3dOptions: ...
