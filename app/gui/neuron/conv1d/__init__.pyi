from lib.gui.element.form import FormInput
from lib.gui.element.switcher import Switcher
from lib.gui.layout import Layout

from app.network.neuron.conv1d.params import Conv1dParams
from app.network.neuron.conv1d.options import Conv1dOptions
from app.network.neuron.conv1d.dimension.params import Conv1dDimensionParams
from app.network.neuron.conv1d.dimension.options import Conv1dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams

from .view import Dimension1dSwitcher, Dimension1dView, Dimension1dDependencies
from .dependencies import Convolution1dStrategyDependencies, InitParamCallback, InitOptionCallback
from .dimension.dependencies import SingleDimensionStrategyDependencies


# Main

class NeuronBuilderConvolution1dStrategy(
    NeuronStrategy[Convolution1dStrategyDependencies, Conv1dParams, Conv1dOptions]
):
    DIMENSION_SWITCHER = ... #type: str

    _input_channels: FormInput[int]
    _output_channels: FormInput[int]
    _groups: FormInput[int]
    _bias: FormInput[bool]

    _input_height: int

    def __init__(self, dependencies: Convolution1dStrategyDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[Conv1dParams, Conv1dOptions]: ...

    @property
    def default_params(self) -> Conv1dParams: ...

    @property
    def default_options(self) -> Conv1dOptions: ...

    @property
    def dimension_params(self) -> NeuronStrategyParams[Conv1dDimensionParams, Conv1dDimensionOptions]: ...

    @property
    def init_param(self) -> InitParamCallback: ...

    @property
    def init_option(self) -> InitOptionCallback: ...

    @property
    def dimension_switcher_program(self) -> Dimension1dSwitcher: ...

    @staticmethod
    def init_switcher(switcher: Switcher[Dimension1dView, Dimension1dDependencies, Conv1dDimensionParams]) -> bool: ...

    def render(self, root: MainWindow) -> Layout: ...
