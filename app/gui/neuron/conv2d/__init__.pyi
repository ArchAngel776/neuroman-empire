from lib.gui.element.form import FormInput
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.conv2d.params import Conv2dParams
from app.network.neuron.conv2d.options import Conv2dOptions
from app.network.neuron.conv2d.dimension.params import Conv2dDimensionParams
from app.network.neuron.conv2d.dimension.options import Conv2dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams

from .view import Dimension2dSwitcher
from .dependencies import Convolution2dStrategyDependencies, InitParamCallback, InitOptionCallback


# Main

class NeuronBuilderConvolution2dStrategy(
    NeuronStrategy[Convolution2dStrategyDependencies, Conv2dParams, Conv2dOptions]
):
    DIMENSION_SWITCHER = ... #type: str

    _input_channels: FormInput[int]
    _output_channels: FormInput[int]
    _groups: FormInput[int]
    _bias: FormInput[bool]

    _reflection: FormInput[bool]

    _input_height: int

    def __init__(self, dependencies: Convolution2dStrategyDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[Conv2dParams, Conv2dOptions]: ...

    @property
    def default_params(self) -> Conv2dParams: ...

    @property
    def default_options(self) -> Conv2dOptions: ...

    @property
    def dimension_params(self) -> NeuronStrategyParams[Conv2dDimensionParams, Conv2dDimensionOptions]: ...

    @property
    def init_param(self) -> InitParamCallback: ...

    @property
    def init_option(self) -> InitOptionCallback: ...

    def change_dimension(self, event: CheckBoxChangedEvent) -> bool: ...

    @property
    def dimension_switcher_program(self) -> Dimension2dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
