from lib import void
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.adaptivemaxpool3d.dimension.params import AdaptiveMaxPool3dDimensionParams
from app.network.neuron.adaptivemaxpool3d.dimension.options import AdaptiveMaxPool3dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams


# Main

class TripleDimensionStrategy(NeuronStrategy[AdaptiveMaxPool3dDimensionParams, AdaptiveMaxPool3dDimensionOptions]):
    class Dimension(int):
        DEPTH = ... #type: TripleDimensionStrategy.Dimension
        HEIGHT = ... #type: TripleDimensionStrategy.Dimension
        WIDTH = ... #type: TripleDimensionStrategy.Dimension

    _output_size_depth: FormInput[int]

    _output_size_height: FormInput[int]

    _output_size_width: FormInput[int]

    _output_enabled_depth: FormInput[bool]

    _output_enabled_height: FormInput[bool]

    _output_enabled_width: FormInput[bool]

    _input_height: int
    _font_caption_title: Font

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[AdaptiveMaxPool3dDimensionParams, AdaptiveMaxPool3dDimensionOptions]: ...

    @property
    def default_params(self) -> AdaptiveMaxPool3dDimensionParams: ...

    @property
    def default_options(self) -> AdaptiveMaxPool3dDimensionOptions: ...

    def load(self, params: AdaptiveMaxPool3dDimensionParams, options: AdaptiveMaxPool3dDimensionOptions) -> void: ...

    def enable_depth(self, event: CheckBoxChangedEvent) -> bool: ...

    def enable_height(self, event: CheckBoxChangedEvent) -> bool: ...

    def enable_width(self, event: CheckBoxChangedEvent) -> bool: ...

    def render(self, root: MainWindow) -> Layout: ...
