from lib import void
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout

from app.network.neuron.adaptiveavgpool2d.dimension.params import AdaptiveAvgPool2dDimensionParams
from app.network.neuron.adaptiveavgpool2d.dimension.options import AdaptiveAvgPool2dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams


# Main

class DoubleDimensionStrategy(NeuronStrategy[AdaptiveAvgPool2dDimensionParams, AdaptiveAvgPool2dDimensionOptions]):
    class Dimension(int):
        HEIGHT = ... #type: DoubleDimensionStrategy.Dimension
        WIDTH = ... #type: DoubleDimensionStrategy.Dimension

    _output_size_height: FormInput[int]

    _output_size_width: FormInput[int]

    _input_height: int
    _font_caption_title: Font

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[AdaptiveAvgPool2dDimensionParams, AdaptiveAvgPool2dDimensionOptions]: ...

    @property
    def default_params(self) -> AdaptiveAvgPool2dDimensionParams: ...

    @property
    def default_options(self) -> AdaptiveAvgPool2dDimensionOptions: ...

    def load(self, params: AdaptiveAvgPool2dDimensionParams, options: AdaptiveAvgPool2dDimensionOptions) -> void: ...

    def render(self, root: MainWindow) -> Layout: ...
