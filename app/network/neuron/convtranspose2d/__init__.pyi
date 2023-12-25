from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import ConvTranspose2dParams
from .options import ConvTranspose2dOptions


# Main

class TransposedConvolution2d(Neuron[ConvTranspose2dParams, ConvTranspose2dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> ConvTranspose2dParams: ...

    @staticmethod
    def default_options() -> ConvTranspose2dOptions: ...
