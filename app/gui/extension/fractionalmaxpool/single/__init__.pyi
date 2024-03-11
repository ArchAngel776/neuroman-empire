from lib import void
from lib.gui.element.form import FormInput
from lib.gui.event.radio_button_toggled import RadioButtonToggled
from lib.gui.layout import Layout

from app.network.extension.fractionalmaxpool.single.params import FractionalMaxPoolSingleDimensionParams
from app.network.extension.fractionalmaxpool.single.options import FractionalMaxPoolSingleDimensionOptions
from app.network.extension.fractionalmaxpool.single.options.output import Output
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams
from .output import OutputSwitcher, OutputParams


# Main

class SingleDimensionStrategy(
    NeuronStrategy[FractionalMaxPoolSingleDimensionParams, FractionalMaxPoolSingleDimensionOptions]
):
    class Watch(str):
        OUTPUT_SWITCHER = ... #type: SingleDimensionStrategy.Watch

    _kernel_size: FormInput[int]

    _output: FormInput[Output]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[
        FractionalMaxPoolSingleDimensionParams, FractionalMaxPoolSingleDimensionOptions
    ]: ...

    @property
    def default_params(self) -> FractionalMaxPoolSingleDimensionParams: ...

    @property
    def default_options(self) -> FractionalMaxPoolSingleDimensionOptions: ...

    def load(
            self,
            params: FractionalMaxPoolSingleDimensionParams,
            options: FractionalMaxPoolSingleDimensionOptions
    ) -> void: ...

    @property
    def output_params(self) -> OutputParams: ...

    def toggle_output(self, event: RadioButtonToggled[Output]) -> bool: ...

    @property
    def output_switcher_program(self) -> OutputSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
