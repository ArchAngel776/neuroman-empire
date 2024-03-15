from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType
from app.network.neuron.adaptiveavgpool3d.params import AdaptiveAvgPool3dParams
from app.network.neuron.adaptiveavgpool3d.options import AdaptiveAvgPool3dOptions


# Main

class AdaptiveAveragePooling3d(Neuron):
    @staticmethod
    def type():
        return NeuronType.ADAPTIVEAVGPOOL3D

    @staticmethod
    def title():
        return "Adaptive Average Pooling 3D"

    @staticmethod
    def default_params():
        return AdaptiveAvgPool3dParams(
            output_size=(1, 1, 1)
        )

    @staticmethod
    def default_options():
        return AdaptiveAvgPool3dOptions(
            cube=False,
            output_enabled=(True, True, True)
        )
