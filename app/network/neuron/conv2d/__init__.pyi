from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import Conv2dParams
from .options import Conv2dOptions


# Main

class Convolution2d(Neuron[Conv2dParams, Conv2dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> Conv2dParams: ...

    @staticmethod
    def default_options() -> Conv2dOptions: ...
