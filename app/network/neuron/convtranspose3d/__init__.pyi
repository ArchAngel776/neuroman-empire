from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import ConvTranspose3dParams
from .options import ConvTranspose3dOptions


# Main

class TransposedConvolution3d(Neuron[ConvTranspose3dParams, ConvTranspose3dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> ConvTranspose3dParams: ...

    @staticmethod
    def default_options() -> ConvTranspose3dOptions: ...
