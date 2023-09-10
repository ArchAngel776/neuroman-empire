from lib.gui.element.form import FormInput
from lib.gui.layout import Layout

from app.network.neuron.conv1d.dimension.params import Conv1dDimensionParams
from app.network.neuron.conv1d.dimension.options import Conv1dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.strategy import NeuronStrategy

from .dependencies import SingleDimensionStrategyDependencies, InitParamCallback, InitOptionCallback


# Main

class SingleDimensionStrategy(
    NeuronStrategy[SingleDimensionStrategyDependencies, Conv1dDimensionParams, Conv1dDimensionOptions]
):
    _kernel_size: FormInput[int]
    _stride: FormInput[int]
    _padding: FormInput[int]
    _dilation: FormInput[int]

    _input_height: int

    def __init__(self, dependencies: SingleDimensionStrategyDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[Conv1dDimensionParams, Conv1dDimensionOptions]: ...

    @property
    def default_params(self) -> Conv1dDimensionParams: ...

    @property
    def default_options(self) -> Conv1dDimensionOptions: ...

    @property
    def init_param(self) -> InitParamCallback: ...

    @property
    def init_option(self) -> InitOptionCallback: ...

    def render(self, root: MainWindow) -> Layout: ...