from typing import Union

from lib.gui.element.switcher.program import SwitcherProgram

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

    _linear_strategy: NeuronBuilderLinearStrategy

    def __init__(self, key: NeuronType, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def strategy(self) -> dict[NeuronType, NeuronStrategy[NeuronParams, NeuronOptions]]: ...
