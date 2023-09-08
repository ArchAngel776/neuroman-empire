from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import Conv1dParams
from .options import Conv1dOptions


# Main

class Convolution1d(Neuron[Conv1dParams, Conv1dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> Conv1dParams: ...

    @staticmethod
    def default_options() -> Conv1dOptions: ...
