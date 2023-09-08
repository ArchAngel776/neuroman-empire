from lib.gui.element.switcher.program import SwitcherProgram

from app.network.neuron.type import NeuronType
from app.gui.neuron.conv1d import NeuronBuilderConvolution1dStrategy
from app.gui.neuron.conv2d import NeuronBuilderConvolution2dStrategy
from app.gui.neuron.conv3d import NeuronBuilderConvolution3dStrategy
from app.gui.neuron.linear import NeuronBuilderLinearStrategy


# Switcher

class NeuronBuilderSwitcher(SwitcherProgram):
    def __init__(self, key, dependencies):
        super().__init__(key, dependencies)
        self._convolution1d_strategy = NeuronBuilderConvolution1dStrategy(dependencies)
        self._convolution2d_strategy = NeuronBuilderConvolution2dStrategy(dependencies)
        self._convolution3d_strategy = NeuronBuilderConvolution3dStrategy(dependencies)
        self._linear_strategy = NeuronBuilderLinearStrategy(dependencies)

    @property
    def strategy(self):
        return {
            NeuronType.CONV1D: self._convolution1d_strategy,
            NeuronType.CONV2D: self._convolution2d_strategy,
            NeuronType.CONV3D: self._convolution3d_strategy,
            NeuronType.LINEAR: self._linear_strategy
        }
