from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import AvgPool3dParams
from .options import AvgPool3dOptions


# Main

class MaxPooling3d(Neuron[AvgPool3dParams, AvgPool3dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> AvgPool3dParams: ...

    @staticmethod
    def default_options() -> AvgPool3dOptions: ...
