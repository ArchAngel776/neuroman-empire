from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import AdaptiveAvgPool3dParams
from .options import AdaptiveAvgPool3dOptions


# Main

class AdaptiveAveragePooling3d(Neuron[AdaptiveAvgPool3dParams, AdaptiveAvgPool3dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> AdaptiveAvgPool3dParams: ...

    @staticmethod
    def default_options() -> AdaptiveAvgPool3dOptions: ...
