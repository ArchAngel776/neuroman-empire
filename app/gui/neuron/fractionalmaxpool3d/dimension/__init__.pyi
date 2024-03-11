from lib import void
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.event.radio_button_toggled import RadioButtonToggled
from lib.gui.layout import Layout

from app.network.neuron.fractionalmaxpool3d.dimension.params import FractionalMaxPool3dDimensionParams
from app.network.neuron.fractionalmaxpool3d.dimension.options import FractionalMaxPool3dDimensionOptions
from app.network.neuron.fractionalmaxpool3d.dimension.options.output import Output
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams
from .output import OutputSwitcher, OutputParams


# Main

class TripleDimensionStrategy(NeuronStrategy[FractionalMaxPool3dDimensionParams, FractionalMaxPool3dDimensionOptions]):
    class Watch(str):
        OUTPUT_SWITCHER = ... #type: TripleDimensionStrategy.Watch

    class Dimension(int):
        DEPTH = ... #type: TripleDimensionStrategy.Dimension
        HEIGHT = ... #type: TripleDimensionStrategy.Dimension
        WIDTH = ... #type: TripleDimensionStrategy.Dimension

    _kernel_size_depth: FormInput[int]

    _kernel_size_height: FormInput[int]

    _kernel_size_width: FormInput[int]

    _output: FormInput[Output]

    _input_height: int
    _font_caption_title: Font

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[FractionalMaxPool3dDimensionParams, FractionalMaxPool3dDimensionOptions]: ...

    @property
    def default_params(self) -> FractionalMaxPool3dDimensionParams: ...

    @property
    def default_options(self) -> FractionalMaxPool3dDimensionOptions: ...

    def load(self, params: FractionalMaxPool3dDimensionParams, options: FractionalMaxPool3dDimensionOptions) -> void: ...

    @property
    def output_params(self) -> OutputParams: ...

    def toggle_output(self, event: RadioButtonToggled[Output]) -> bool: ...

    @property
    def output_switcher_program(self) -> OutputSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
