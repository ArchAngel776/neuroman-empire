from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import FractionalMaxPool3dParams
from .options import FractionalMaxPool3dOptions


# Main

class FractionalMaxPooling3d(Neuron[FractionalMaxPool3dParams, FractionalMaxPool3dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> FractionalMaxPool3dParams: ...

    @staticmethod
    def default_options() -> FractionalMaxPool3dOptions: ...
