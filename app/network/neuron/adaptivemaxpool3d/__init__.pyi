from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import AdaptiveMaxPool3dParams
from .options import AdaptiveMaxPool3dOptions


# Main

class AdaptiveMaxPooling3d(Neuron[AdaptiveMaxPool3dParams, AdaptiveMaxPool3dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> AdaptiveMaxPool3dParams: ...

    @staticmethod
    def default_options() -> AdaptiveMaxPool3dOptions: ...
