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
    MAXUNPOOL1D = ... #type: NeuronType
    MAXUNPOOL2D = ... #type: NeuronType
    MAXUNPOOL3D = ... #type: NeuronType
    AVGPOOL1D = ...  #type:NeuronType
    AVGPOOL2D = ...  #type:NeuronType
    AVGPOOL3D = ...  #type:NeuronType
    FRACTIONALMAXPOOL2D = ...  #type:NeuronType
    FRACTIONALMAXPOOL3D = ...  #type:NeuronType
    LPPOOL1D = ...  #type:NeuronType
    LPPOOL2D = ...  #type:NeuronType
    LINEAR = ... #type: NeuronType
