from enum import Enum


# Main

class NeuronType(Enum):
    CONV1D = "conv1d"
    CONV2D = "conv2d"
    CONV3D = "conv3d"
    CONVTRANSPOSE1D = "convtranspose1d"
    CONVTRANSPOSE2D = "convtranspose2d"
    CONVTRANSPOSE3D = "convtranspose3d"
    UNFOLD = "unfold"
    FOLD = "fold"
    MAXPOOL1D = "maxpool1d"
    MAXPOOL2D = "maxpool2d"
    MAXPOOL3D = "maxpool3d"
    MAXUNPOOL1D = "maxunpool1d"
    MAXUNPOOL2D = "maxunpool2d"
    MAXUNPOOL3D = "maxunpool3d"
    AVGPOOL1D = "avgpool1d"
    AVGPOOL2D = "avgpool2d"
    AVGPOOL3D = "avgpool3d"
    FRACTIONALMAXPOOL2D = "fractionalmaxpool2d"
    FRACTIONALMAXPOOL3D = "fractionalmaxpool3d"
    LINEAR = "linear"
