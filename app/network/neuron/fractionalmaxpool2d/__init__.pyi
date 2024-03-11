from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import FractionalMaxPool2dParams
from .options import FractionalMaxPool2dOptions


# Main

class FractionalMaxPooling2d(Neuron[FractionalMaxPool2dParams, FractionalMaxPool2dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> FractionalMaxPool2dParams: ...

    @staticmethod
    def default_options() -> FractionalMaxPool2dOptions: ...
