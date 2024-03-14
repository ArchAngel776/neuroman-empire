from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType
from app.network.neuron.adaptivemaxpool3d.params import AdaptiveMaxPool3dParams
from app.network.neuron.adaptivemaxpool3d.options import AdaptiveMaxPool3dOptions


# Main

class AdaptiveMaxPooling3d(Neuron):
    @staticmethod
    def type():
        return NeuronType.ADAPTIVEMAXPOOL3D

    @staticmethod
    def title():
        return "Adaptive Max Pooling 3D"

    @staticmethod
    def default_params():
        return AdaptiveMaxPool3dParams(
            output_size=(1, 1, 1),
            return_indices=False
        )

    @staticmethod
    def default_options():
        return AdaptiveMaxPool3dOptions(
            cube=False
        )
