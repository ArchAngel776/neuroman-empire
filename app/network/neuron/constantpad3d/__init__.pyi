from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import ConstantPad3dParams
from .options import ConstantPad3dOptions


# Main

class ConstantPadding3d(Neuron[ConstantPad3dParams, ConstantPad3dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> ConstantPad3dParams: ...

    @staticmethod
    def default_options() -> ConstantPad3dOptions: ...
