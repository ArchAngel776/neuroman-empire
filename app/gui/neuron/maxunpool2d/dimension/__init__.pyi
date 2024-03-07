from lib import void
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout

from app.network.neuron.maxunpool2d.dimension.params import MaxUnpool2dDimensionParams
from app.network.neuron.maxunpool2d.dimension.options import MaxUnpool2dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams


# Main

class DoubleDimensionStrategy(NeuronStrategy[MaxUnpool2dDimensionParams, MaxUnpool2dDimensionOptions]):
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
    def params(self) -> NeuronStrategyParams[MaxUnpool2dDimensionParams, MaxUnpool2dDimensionOptions]: ...

    @property
    def default_params(self) -> MaxUnpool2dDimensionParams: ...

    @property
    def default_options(self) -> MaxUnpool2dDimensionOptions: ...

    def load(self, params: MaxUnpool2dDimensionParams, options: MaxUnpool2dDimensionOptions) -> void: ...

    def render(self, root: MainWindow) -> Layout: ...
