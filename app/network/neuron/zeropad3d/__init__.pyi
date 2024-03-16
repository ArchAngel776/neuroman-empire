from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import ZeroPad3dParams
from .options import ZeroPad3dOptions


# Main

class ZeroPadding3d(Neuron[ZeroPad3dParams, ZeroPad3dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> ZeroPad3dParams: ...

    @staticmethod
    def default_options() -> ZeroPad3dOptions: ...
