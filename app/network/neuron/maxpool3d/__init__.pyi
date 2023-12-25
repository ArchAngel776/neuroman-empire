from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType

from .params import MaxPool3dParams
from .options import MaxPool3dOptions


# Main

class MaxPooling3d(Neuron[MaxPool3dParams, MaxPool3dOptions]):
    @staticmethod
    def type() -> NeuronType: ...

    @staticmethod
    def title() -> str: ...

    @staticmethod
    def default_params() -> MaxPool3dParams: ...

    @staticmethod
    def default_options() -> MaxPool3dOptions: ...
