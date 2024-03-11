from lib import void
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.event.radio_button_toggled import RadioButtonToggled
from lib.gui.layout import Layout

from app.network.neuron.fractionalmaxpool2d.dimension.params import FractionalMaxPool2dDimensionParams
from app.network.neuron.fractionalmaxpool2d.dimension.options import FractionalMaxPool2dDimensionOptions
from app.network.neuron.fractionalmaxpool2d.dimension.options.output import Output
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams
from .output import OutputSwitcher, OutputParams


# Main

class DoubleDimensionStrategy(NeuronStrategy[FractionalMaxPool2dDimensionParams, FractionalMaxPool2dDimensionOptions]):
    class Watch(str):
        OUTPUT_SWITCHER = ... #type: DoubleDimensionStrategy.Watch

    class Dimension(int):
        HEIGHT = ... #type: DoubleDimensionStrategy.Dimension
        WIDTH = ... #type: DoubleDimensionStrategy.Dimension

    _kernel_size_height: FormInput[int]

    _kernel_size_width: FormInput[int]

    _output: FormInput[Output]

    _input_height: int
    _font_caption_title: Font

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[FractionalMaxPool2dDimensionParams, FractionalMaxPool2dDimensionOptions]: ...

    @property
    def default_params(self) -> FractionalMaxPool2dDimensionParams: ...

    @property
    def default_options(self) -> FractionalMaxPool2dDimensionOptions: ...

    def load(self, params: FractionalMaxPool2dDimensionParams, options: FractionalMaxPool2dDimensionOptions) -> void: ...

    @property
    def output_params(self) -> OutputParams: ...

    def toggle_output(self, event: RadioButtonToggled[Output]) -> bool: ...

    @property
    def output_switcher_program(self) -> OutputSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
