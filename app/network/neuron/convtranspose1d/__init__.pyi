from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import ConvTranspose1dParams
from .options import ConvTranspose1dOptions


# Main

class TransposedConvolution1d(Neuron[ConvTranspose1dParams, ConvTranspose1dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> ConvTranspose1dParams: ...

    @staticmethod
    def default_options() -> ConvTranspose1dOptions: ...
