from app.network.neuron import Neuron
from app.network.neuron.type import NeuronType
from app.network.neuron.avgpool3d.params import AvgPool3dParams
from app.network.neuron.avgpool3d.options import AvgPool3dOptions


# Main

class AveragePooling3d(Neuron):
    @staticmethod
    def type():
        return NeuronType.AVGPOOL3D

    @staticmethod
    def title():
        return "Average Pooling 3D"

    @staticmethod
    def default_params():
        return AvgPool3dParams(
            ceil_mode=True,
            kernel_size=(1, 1, 1),
            stride=(1, 1, 1),
            padding=(0, 0, 0),
            count_include_pad=True,
            divisor_override=1
        )

    @staticmethod
    def default_options():
        return AvgPool3dOptions(
            cube=False,
            divisor_enabled=False
        )
