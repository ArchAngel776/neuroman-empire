from lib.gui.element.component.switcher.program import SwitcherProgram

from app.network.neuron.type import NeuronType

from app.gui.neuron.conv1d import NeuronBuilderConvolution1dStrategy
from app.gui.neuron.conv2d import NeuronBuilderConvolution2dStrategy
from app.gui.neuron.conv3d import NeuronBuilderConvolution3dStrategy
from app.gui.neuron.convtranspose1d import NeuronBuilderTransposedConvolution1dStrategy
from app.gui.neuron.convtranspose2d import NeuronBuilderTransposedConvolution2dStrategy
from app.gui.neuron.convtranspose3d import NeuronBuilderTransposedConvolution3dStrategy
from app.gui.neuron.unfold import NeuronBuilderUnfoldStrategy
from app.gui.neuron.fold import NeuronBuilderFoldStrategy
from app.gui.neuron.maxpool1d import NeuronBuilderMaxPooling1dStrategy
from app.gui.neuron.maxpool2d import NeuronBuilderMaxPooling2dStrategy
from app.gui.neuron.maxpool3d import NeuronBuilderMaxPooling3dStrategy
from app.gui.neuron.maxunpool1d import NeuronBuilderMaxUnpooling1dStrategy
from app.gui.neuron.maxunpool2d import NeuronBuilderMaxUnpooling2dStrategy
from app.gui.neuron.maxunpool3d import NeuronBuilderMaxUnpooling3dStrategy
from app.gui.neuron.avgpool1d import NeuronBuilderAveragePooling1dStrategy
from app.gui.neuron.avgpool2d import NeuronBuilderAveragePooling2dStrategy
from app.gui.neuron.avgpool3d import NeuronBuilderAveragePooling3dStrategy
from app.gui.neuron.fractionalmaxpool2d import NeuronBuilderFractionalMaxPooling2dStrategy
from app.gui.neuron.fractionalmaxpool3d import NeuronBuilderFractionalMaxPooling3dStrategy
from app.gui.neuron.linear import NeuronBuilderLinearStrategy


# Switcher

class NeuronBuilderSwitcher(SwitcherProgram):
    def __init__(self, key, dependencies):
        super().__init__(key, dependencies)

        self._convolution1d_strategy = NeuronBuilderConvolution1dStrategy(dependencies)
        self._convolution2d_strategy = NeuronBuilderConvolution2dStrategy(dependencies)
        self._convolution3d_strategy = NeuronBuilderConvolution3dStrategy(dependencies)

        self._transposed_convolution1d_strategy = NeuronBuilderTransposedConvolution1dStrategy(dependencies)
        self._transposed_convolution2d_strategy = NeuronBuilderTransposedConvolution2dStrategy(dependencies)
        self._transposed_convolution3d_strategy = NeuronBuilderTransposedConvolution3dStrategy(dependencies)

        self._unfold_strategy = NeuronBuilderUnfoldStrategy(dependencies)
        self._fold_strategy = NeuronBuilderFoldStrategy(dependencies)

        self._max_pooling1d_strategy = NeuronBuilderMaxPooling1dStrategy(dependencies)
        self._max_pooling2d_strategy = NeuronBuilderMaxPooling2dStrategy(dependencies)
        self._max_pooling3d_strategy = NeuronBuilderMaxPooling3dStrategy(dependencies)

        self._max_unpooling1d_strategy = NeuronBuilderMaxUnpooling1dStrategy(dependencies)
        self._max_unpooling2d_strategy = NeuronBuilderMaxUnpooling2dStrategy(dependencies)
        self._max_unpooling3d_strategy = NeuronBuilderMaxUnpooling3dStrategy(dependencies)

        self._average_pooling1d_strategy = NeuronBuilderAveragePooling1dStrategy(dependencies)
        self._average_pooling2d_strategy = NeuronBuilderAveragePooling2dStrategy(dependencies)
        self._average_pooling3d_strategy = NeuronBuilderAveragePooling3dStrategy(dependencies)

        self._fractional_max_pooling2d_strategy = NeuronBuilderFractionalMaxPooling2dStrategy(dependencies)
        self._fractional_max_pooling3d_strategy = NeuronBuilderFractionalMaxPooling3dStrategy(dependencies)

        self._linear_strategy = NeuronBuilderLinearStrategy(dependencies)

    @property
    def strategy(self):
        return {
            NeuronType.CONV1D: self._convolution1d_strategy,
            NeuronType.CONV2D: self._convolution2d_strategy,
            NeuronType.CONV3D: self._convolution3d_strategy,
            NeuronType.CONVTRANSPOSE1D: self._transposed_convolution1d_strategy,
            NeuronType.CONVTRANSPOSE2D: self._transposed_convolution2d_strategy,
            NeuronType.CONVTRANSPOSE3D: self._transposed_convolution3d_strategy,
            NeuronType.UNFOLD: self._unfold_strategy,
            NeuronType.FOLD: self._fold_strategy,
            NeuronType.MAXPOOL1D: self._max_pooling1d_strategy,
            NeuronType.MAXPOOL2D: self._max_pooling2d_strategy,
            NeuronType.MAXPOOL3D: self._max_pooling3d_strategy,
            NeuronType.MAXUNPOOL1D: self._max_unpooling1d_strategy,
            NeuronType.MAXUNPOOL2D: self._max_unpooling2d_strategy,
            NeuronType.MAXUNPOOL3D: self._max_unpooling3d_strategy,
            NeuronType.AVGPOOL1D: self._average_pooling1d_strategy,
            NeuronType.AVGPOOL2D: self._average_pooling2d_strategy,
            NeuronType.AVGPOOL3D: self._average_pooling3d_strategy,
            NeuronType.FRACTIONALMAXPOOL2D: self._fractional_max_pooling2d_strategy,
            NeuronType.FRACTIONALMAXPOOL3D: self._fractional_max_pooling3d_strategy,
            NeuronType.LINEAR: self._linear_strategy
        }
