from lib import void
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.adaptivemaxpool2d.dimension.params import AdaptiveMaxPool2dDimensionParams
from app.network.neuron.adaptivemaxpool2d.dimension.options import AdaptiveMaxPool2dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams


# Main

class DoubleDimensionStrategy(NeuronStrategy[AdaptiveMaxPool2dDimensionParams, AdaptiveMaxPool2dDimensionOptions]):
    class Dimension(int):
        HEIGHT = ... #type: DoubleDimensionStrategy.Dimension
        WIDTH = ... #type: DoubleDimensionStrategy.Dimension

    _output_size_height: FormInput[int]

    _output_size_width: FormInput[int]

    _output_enabled_height: FormInput[bool]

    _output_enabled_width: FormInput[bool]

    _input_height: int
    _font_caption_title: Font

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[AdaptiveMaxPool2dDimensionParams, AdaptiveMaxPool2dDimensionOptions]: ...

    @property
    def default_params(self) -> AdaptiveMaxPool2dDimensionParams: ...

    @property
    def default_options(self) -> AdaptiveMaxPool2dDimensionOptions: ...

    def load(self, params: AdaptiveMaxPool2dDimensionParams, options: AdaptiveMaxPool2dDimensionOptions) -> void: ...

    def enable_height(self, event: CheckBoxChangedEvent) -> bool: ...

    def enable_width(self, event: CheckBoxChangedEvent) -> bool: ...

    def render(self, root: MainWindow) -> Layout: ...
