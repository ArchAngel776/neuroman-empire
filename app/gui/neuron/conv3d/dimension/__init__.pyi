from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout

from app.network.neuron.conv3d.dimension.params import Conv3dDimensionParams
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy

from .dependencies import TripleDimensionStrategyDependencies


# Main

class TripleDimensionStrategy(NeuronStrategy[TripleDimensionStrategyDependencies, Conv3dDimensionParams, {}]):
    class Dimension(int):
        DEPTH = ... #type: TripleDimensionStrategy.Dimension
        HEIGHT = ... #type: TripleDimensionStrategy.Dimension
        WIDTH = ... #type: TripleDimensionStrategy.Dimension

    _kernel_size_depth: FormInput[int]
    _stride_depth: FormInput[int]
    _padding_depth: FormInput[int]
    _dilation_depth: FormInput[int]

    _kernel_size_height: FormInput[int]
    _stride_height: FormInput[int]
    _padding_height: FormInput[int]
    _dilation_height: FormInput[int]

    _kernel_size_width: FormInput[int]
    _stride_width: FormInput[int]
    _padding_width: FormInput[int]
    _dilation_width: FormInput[int]

    _input_height: int
    _font_caption_title: Font

    def __init__(self, dependencies: TripleDimensionStrategyDependencies) -> None: ...

    @property
    def params(self) -> Conv3dDimensionParams: ...

    @property
    def default_params(self) -> Conv3dDimensionParams: ...

    @property
    def default_options(self) -> {}: ...

    def render(self, root: MainWindow) -> Layout: ...
