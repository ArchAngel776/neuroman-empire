from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import UnfoldParams
from .options import UnfoldOptions


# Main

class Unfold(Neuron[UnfoldParams, UnfoldOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> UnfoldParams: ...

    @staticmethod
    def default_options() -> UnfoldOptions: ...
