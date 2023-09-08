from typing import Union

from lib.gui.element.switcher.program import SwitcherProgram
from lib.gui.element.switcher.strategy import SwitcherStrategy

from app.network.neuron.type import NeuronType
from app.network.neuron.conv1d.params import Conv1dParams
from app.network.neuron.conv2d.params import Conv2dParams
from app.network.neuron.conv3d.params import Conv3dParams
from app.network.neuron.linear.params import LinearParams

from .conv1d import NeuronBuilderConvolution1dStrategy
from .conv2d import NeuronBuilderConvolution2dStrategy
from .conv3d import NeuronBuilderConvolution3dStrategy
from .linear import NeuronBuilderLinearStrategy
from .conv1d.dependencies import Convolution1dStrategyDependencies
from .conv2d.dependencies import Convolution2dStrategyDependencies
from .conv3d.dependencies import Convolution3dStrategyDependencies
from .linear.dependencies import LinearStrategyDependencies

# Types

NeuronDependencies = Union[
    Convolution1dStrategyDependencies,
    Convolution2dStrategyDependencies,
    Convolution3dStrategyDependencies,
    LinearStrategyDependencies
]

NeuronParams = Union[
    Conv1dParams,
    Conv2dParams,
    Conv3dParams,
    LinearParams
]


# Switcher

class NeuronBuilderSwitcher(SwitcherProgram[NeuronType, NeuronDependencies, NeuronParams]):
    _convolution1d_strategy: NeuronBuilderConvolution1dStrategy
    _convolution2d_strategy: NeuronBuilderConvolution2dStrategy
    _convolution3d_strategy: NeuronBuilderConvolution3dStrategy
    _linear_strategy: NeuronBuilderLinearStrategy

    def __init__(self, key: NeuronType, dependencies: NeuronDependencies) -> None: ...

    @property
    def strategy(self) -> dict[NeuronType, SwitcherStrategy[NeuronDependencies, NeuronParams]]: ...
