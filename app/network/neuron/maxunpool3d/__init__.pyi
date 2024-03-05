from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import MaxUnpool3dParams
from .options import MaxUnpool3dOptions


# Main

class MaxUnpooling1d(Neuron[MaxUnpool3dParams, MaxUnpool3dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> MaxUnpool3dParams: ...

    @staticmethod
    def default_options() -> MaxUnpool3dOptions: ...
