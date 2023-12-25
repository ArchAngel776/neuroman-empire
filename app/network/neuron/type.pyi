from enum import Enum


# Main

class NeuronType(Enum):
    CONV1D = ... #type: NeuronType
    CONV2D = ... #type: NeuronType
    CONV3D = ... #type: NeuronType
    CONVTRANSPOSE1D = ... #type: NeuronType
    CONVTRANSPOSE2D = ... #type: NeuronType
    CONVTRANSPOSE3D = ... #type: NeuronType
    UNFOLD = ... #type: NeuronType
    FOLD = ... #type: NeuronType
    MAXPOOL1D = ... #type:NeuronType
    MAXPOOL2D = ... #type:NeuronType
    MAXPOOL3D = ... #type:NeuronType
    LINEAR = ... #type: NeuronType
