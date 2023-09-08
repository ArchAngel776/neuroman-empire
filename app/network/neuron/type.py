from enum import Enum


# Main

class NeuronType(Enum):
    CONV1D = "conv1d"
    CONV2D = "conv2d"
    CONV3D = "conv3d"
    LINEAR = "linear"
