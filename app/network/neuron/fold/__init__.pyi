from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import FoldParams
from .options import FoldOptions


# Main

class Fold(Neuron[FoldParams, FoldOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> FoldParams: ...

    @staticmethod
    def default_options() -> FoldOptions: ...
