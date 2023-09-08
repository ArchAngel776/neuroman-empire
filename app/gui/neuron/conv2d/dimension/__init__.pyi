from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout

from app.network.neuron.conv2d.dimension.params import Conv2dDimensionParams
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy

from .dependencies import DoubleDimensionStrategyDependencies


# Main

class DoubleDimensionStrategy(NeuronStrategy[DoubleDimensionStrategyDependencies, Conv2dDimensionParams, {}]):
    class Dimension(int):
        HEIGHT = ... #type: DoubleDimensionStrategy.Dimension
        WIDTH = ... #type: DoubleDimensionStrategy.Dimension

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

    def __init__(self, dependencies: DoubleDimensionStrategyDependencies) -> None: ...

    @property
    def params(self) -> Conv2dDimensionParams: ...

    @property
    def default_params(self) -> Conv2dDimensionParams: ...

    @property
    def default_options(self) -> {}: ...

    def render(self, root: MainWindow) -> Layout: ...
