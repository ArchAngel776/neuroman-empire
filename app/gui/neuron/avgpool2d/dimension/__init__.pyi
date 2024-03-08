from lib import void
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout

from app.network.neuron.avgpool2d.dimension.params import AvgPool2dDimensionParams
from app.network.neuron.avgpool2d.dimension.options import AvgPool2dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams


# Main

class DoubleDimensionStrategy(NeuronStrategy[AvgPool2dDimensionParams, AvgPool2dDimensionOptions]):
    class Dimension(int):
        HEIGHT = ... #type: DoubleDimensionStrategy.Dimension
        WIDTH = ... #type: DoubleDimensionStrategy.Dimension

    _kernel_size_height: FormInput[int]
    _stride_height: FormInput[int]
    _padding_height: FormInput[int]

    _kernel_size_width: FormInput[int]
    _stride_width: FormInput[int]
    _padding_width: FormInput[int]

    _input_height: int
    _font_caption_title: Font

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[AvgPool2dDimensionParams, AvgPool2dDimensionOptions]: ...

    @property
    def default_params(self) -> AvgPool2dDimensionParams: ...

    @property
    def default_options(self) -> AvgPool2dDimensionOptions: ...

    def load(self, params: AvgPool2dDimensionParams, options: AvgPool2dDimensionOptions) -> void: ...

    def render(self, root: MainWindow) -> Layout: ...
