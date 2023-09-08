from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import Conv3dParams
from .options import Conv3dOptions


# Main

class Convolution3d(Neuron[Conv3dParams, Conv3dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> Conv3dParams: ...

    @staticmethod
    def default_options() -> Conv3dOptions: ...
