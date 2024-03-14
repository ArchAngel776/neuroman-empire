from typing import Union

from lib.gui.element.component.switcher.program import SwitcherProgram

from app.network.neuron.type import NeuronType
from .dependencies import NeuronBuilderDependencies

from app.network.neuron.conv1d.params import Conv1dParams
from app.network.neuron.conv2d.params import Conv2dParams
from app.network.neuron.conv3d.params import Conv3dParams
from app.network.neuron.convtranspose1d.params import ConvTranspose1dParams
from app.network.neuron.convtranspose2d.params import ConvTranspose2dParams
from app.network.neuron.convtranspose3d.params import ConvTranspose3dParams
from app.network.neuron.unfold.params import UnfoldParams
from app.network.neuron.fold.params import FoldParams
from app.network.neuron.maxpool1d.params import MaxPool1dParams
from app.network.neuron.maxpool2d.params import MaxPool2dParams
from app.network.neuron.maxpool3d.params import MaxPool3dParams
from app.network.neuron.maxunpool1d.params import MaxUnpool1dParams
from app.network.neuron.maxunpool2d.params import MaxUnpool2dParams
from app.network.neuron.maxunpool3d.params import MaxUnpool3dParams
from app.network.neuron.avgpool1d.params import AvgPool1dParams
from app.network.neuron.avgpool2d.params import AvgPool2dParams
from app.network.neuron.avgpool3d.params import AvgPool3dParams
from app.network.neuron.fractionalmaxpool2d.params import FractionalMaxPool2dParams
from app.network.neuron.fractionalmaxpool3d.params import FractionalMaxPool3dParams
from app.network.neuron.lppool1d.params import LPPool1dParams
from app.network.neuron.lppool2d.params import LPPool2dParams
from app.network.neuron.adaptivemaxpool1d.params import AdaptiveMaxPool1dParams
from app.network.neuron.adaptivemaxpool2d.params import AdaptiveMaxPool2dParams
from app.network.neuron.adaptivemaxpool3d.params import AdaptiveMaxPool3dParams
from app.network.neuron.adaptiveavgpool1d.params import AdaptiveAvgPool1dParams
from app.network.neuron.adaptiveavgpool2d.params import AdaptiveAvgPool2dParams
from app.network.neuron.adaptiveavgpool3d.params import AdaptiveAvgPool3dParams
from app.network.neuron.linear.params import LinearParams

from app.network.neuron.conv1d.options import Conv1dOptions
from app.network.neuron.conv2d.options import Conv2dOptions
from app.network.neuron.conv3d.options import Conv3dOptions
from app.network.neuron.convtranspose1d.options import ConvTranspose1dOptions
from app.network.neuron.convtranspose2d.options import ConvTranspose2dOptions
from app.network.neuron.convtranspose3d.options import ConvTranspose3dOptions
from app.network.neuron.unfold.options import UnfoldOptions
from app.network.neuron.fold.options import FoldOptions
from app.network.neuron.maxpool1d.options import MaxPool1dOptions
from app.network.neuron.maxpool2d.options import MaxPool2dOptions
from app.network.neuron.maxpool3d.options import MaxPool3dOptions
from app.network.neuron.maxunpool1d.options import MaxUnpool1dOptions
from app.network.neuron.maxunpool2d.options import MaxUnpool2dOptions
from app.network.neuron.maxunpool3d.options import MaxUnpool3dOptions
from app.network.neuron.avgpool1d.options import AvgPool1dOptions
from app.network.neuron.avgpool2d.options import AvgPool2dOptions
from app.network.neuron.avgpool3d.options import AvgPool3dOptions
from app.network.neuron.fractionalmaxpool2d.options import FractionalMaxPool2dOptions
from app.network.neuron.fractionalmaxpool3d.options import FractionalMaxPool3dOptions
from app.network.neuron.lppool1d.options import LPPool1dOptions
from app.network.neuron.lppool2d.options import LPPool2dOptions
from app.network.neuron.adaptivemaxpool1d.options import AdaptiveMaxPool1dOptions
from app.network.neuron.adaptivemaxpool2d.options import AdaptiveMaxPool2dOptions
from app.network.neuron.adaptivemaxpool3d.options import AdaptiveMaxPool3dOptions
from app.network.neuron.adaptiveavgpool1d.options import AdaptiveAvgPool1dOptions
from app.network.neuron.adaptiveavgpool2d.options import AdaptiveAvgPool2dOptions
from app.network.neuron.adaptiveavgpool3d.options import AdaptiveAvgPool3dOptions
from app.network.neuron.linear.options import LinearOptions

from .strategy import NeuronStrategy
from .params import NeuronStrategyParams
from .conv1d import NeuronBuilderConvolution1dStrategy
from .conv2d import NeuronBuilderConvolution2dStrategy
from .conv3d import NeuronBuilderConvolution3dStrategy
from .convtranspose1d import NeuronBuilderTransposedConvolution1dStrategy
from .convtranspose2d import NeuronBuilderTransposedConvolution2dStrategy
from .convtranspose3d import NeuronBuilderTransposedConvolution3dStrategy
from .unfold import NeuronBuilderUnfoldStrategy
from .fold import NeuronBuilderFoldStrategy
from .maxpool1d import NeuronBuilderMaxPooling1dStrategy
from .maxpool2d import NeuronBuilderMaxPooling2dStrategy
from .maxpool3d import NeuronBuilderMaxPooling3dStrategy
from .maxunpool1d import NeuronBuilderMaxUnpooling1dStrategy
from .maxunpool2d import NeuronBuilderMaxUnpooling2dStrategy
from .maxunpool3d import NeuronBuilderMaxUnpooling3dStrategy
from .avgpool1d import NeuronBuilderAveragePooling1dStrategy
from .avgpool2d import NeuronBuilderAveragePooling2dStrategy
from .avgpool3d import NeuronBuilderAveragePooling3dStrategy
from .fractionalmaxpool2d import NeuronBuilderFractionalMaxPooling2dStrategy
from .fractionalmaxpool3d import NeuronBuilderFractionalMaxPooling3dStrategy
from .lppool1d import NeuronBuilderLocalPooling1dStrategy
from .lppool2d import NeuronBuilderLocalPooling2dStrategy
from .adaptivemaxpool1d import NeuronBuilderAdaptiveMaxPooling1dStrategy
from .adaptivemaxpool2d import NeuronBuilderAdaptiveMaxPooling2dStrategy
from .adaptivemaxpool3d import NeuronBuilderAdaptiveMaxPooling3dStrategy
from .adaptiveavgpool1d import NeuronBuilderAdaptiveAveragePooling1dStrategy
from .adaptiveavgpool2d import NeuronBuilderAdaptiveAveragePooling2dStrategy
from .adaptiveavgpool3d import NeuronBuilderAdaptiveAveragePooling3dStrategy
from .linear import NeuronBuilderLinearStrategy

# Types

NeuronParams = Union[
    Conv1dParams,
    Conv2dParams,
    Conv3dParams,
    ConvTranspose1dParams,
    ConvTranspose2dParams,
    ConvTranspose3dParams,
    UnfoldParams,
    FoldParams,
    MaxPool1dParams,
    MaxPool2dParams,
    MaxPool3dParams,
    MaxUnpool1dParams,
    MaxUnpool2dParams,
    MaxUnpool3dParams,
    AvgPool1dParams,
    AvgPool2dParams,
    AvgPool3dParams,
    FractionalMaxPool2dParams,
    FractionalMaxPool3dParams,
    LPPool1dParams,
    LPPool2dParams,
    AdaptiveMaxPool1dParams,
    AdaptiveMaxPool2dParams,
    AdaptiveMaxPool3dParams,
    AdaptiveAvgPool1dParams,
    AdaptiveAvgPool2dParams,
    AdaptiveAvgPool3dParams,
    LinearParams
]

NeuronOptions = Union[
    Conv1dOptions,
    Conv2dOptions,
    Conv3dOptions,
    ConvTranspose1dOptions,
    ConvTranspose2dOptions,
    ConvTranspose3dOptions,
    UnfoldOptions,
    FoldOptions,
    MaxPool1dOptions,
    MaxPool2dOptions,
    MaxPool3dOptions,
    MaxUnpool1dOptions,
    MaxUnpool2dOptions,
    MaxUnpool3dOptions,
    AvgPool1dOptions,
    AvgPool2dOptions,
    AvgPool3dOptions,
    FractionalMaxPool2dOptions,
    FractionalMaxPool3dOptions,
    LPPool1dOptions,
    LPPool2dOptions,
    AdaptiveMaxPool1dOptions,
    AdaptiveMaxPool2dOptions,
    AdaptiveMaxPool3dOptions,
    AdaptiveAvgPool1dOptions,
    AdaptiveAvgPool2dOptions,
    AdaptiveAvgPool3dOptions,
    LinearOptions
]


# Switcher

class NeuronBuilderSwitcher(
    SwitcherProgram[NeuronType, NeuronBuilderDependencies, NeuronStrategyParams[NeuronParams, NeuronOptions]]
):
    _convolution1d_strategy: NeuronBuilderConvolution1dStrategy
    _convolution2d_strategy: NeuronBuilderConvolution2dStrategy
    _convolution3d_strategy: NeuronBuilderConvolution3dStrategy

    _transposed_convolution1d_strategy: NeuronBuilderTransposedConvolution1dStrategy
    _transposed_convolution2d_strategy: NeuronBuilderTransposedConvolution2dStrategy
    _transposed_convolution3d_strategy: NeuronBuilderTransposedConvolution3dStrategy

    _unfold_strategy: NeuronBuilderUnfoldStrategy
    _fold_strategy: NeuronBuilderFoldStrategy

    _max_pooling1d_strategy: NeuronBuilderMaxPooling1dStrategy
    _max_pooling2d_strategy: NeuronBuilderMaxPooling2dStrategy
    _max_pooling3d_strategy: NeuronBuilderMaxPooling3dStrategy

    _max_unpooling1d_strategy: NeuronBuilderMaxUnpooling1dStrategy
    _max_unpooling2d_strategy: NeuronBuilderMaxUnpooling2dStrategy
    _max_unpooling3d_strategy: NeuronBuilderMaxUnpooling3dStrategy

    _average_pooling1d_strategy: NeuronBuilderAveragePooling1dStrategy
    _average_pooling2d_strategy: NeuronBuilderAveragePooling2dStrategy
    _average_pooling3d_strategy: NeuronBuilderAveragePooling3dStrategy

    _fractional_max_pooling2d_strategy: NeuronBuilderFractionalMaxPooling2dStrategy
    _fractional_max_pooling3d_strategy: NeuronBuilderFractionalMaxPooling3dStrategy

    _local_pooling1d_strategy: NeuronBuilderLocalPooling1dStrategy
    _local_pooling2d_strategy: NeuronBuilderLocalPooling2dStrategy

    _adaptive_max_pooling1d_strategy: NeuronBuilderAdaptiveMaxPooling1dStrategy
    _adaptive_max_pooling2d_strategy: NeuronBuilderAdaptiveMaxPooling2dStrategy
    _adaptive_max_pooling3d_strategy: NeuronBuilderAdaptiveMaxPooling3dStrategy

    _adaptive_average_pooling1d_strategy: NeuronBuilderAdaptiveAveragePooling1dStrategy
    _adaptive_average_pooling2d_strategy: NeuronBuilderAdaptiveAveragePooling2dStrategy
    _adaptive_average_pooling3d_strategy: NeuronBuilderAdaptiveAveragePooling3dStrategy

    _linear_strategy: NeuronBuilderLinearStrategy

    def __init__(self, key: NeuronType, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def strategy(self) -> dict[NeuronType, NeuronStrategy[NeuronParams, NeuronOptions]]: ...
