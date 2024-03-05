from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import MaxUnpool2dParams
from .options import MaxUnpool2dOptions


# Main

class MaxUnpooling2d(Neuron[MaxUnpool2dParams, MaxUnpool2dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> MaxUnpool2dParams: ...

    @staticmethod
    def default_options() -> MaxUnpool2dOptions: ...
