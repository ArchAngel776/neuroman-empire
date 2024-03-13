from lib import void
from lib.gui.element.form import FormInput
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.conv2d.params import Conv2dParams
from app.network.neuron.conv2d.options import Conv2dOptions
from app.network.neuron.conv2d.dimension.params import Conv2dDimensionParams
from app.network.neuron.conv2d.dimension.options import Conv2dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Dimension2dSwitcher, Dimension2dView


# Main

class NeuronBuilderConvolution2dStrategy(NeuronStrategy[Conv2dParams, Conv2dOptions]):
    class Watch(str):
        DIMENSION_SWITCHER = ... #type: NeuronBuilderConvolution2dStrategy.Watch

    _input_channels: FormInput[int]
    _output_channels: FormInput[int]
    _groups: FormInput[int]
    _bias: FormInput[bool]

    _reflection: FormInput[bool]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[Conv2dParams, Conv2dOptions]: ...

    @property
    def default_params(self) -> Conv2dParams: ...

    @property
    def default_options(self) -> Conv2dOptions: ...

    def load(self, params: Conv2dParams, options: Conv2dOptions) -> void: ...

    @property
    def dimension_params(self) -> NeuronStrategyParams[Conv2dDimensionParams, Conv2dDimensionOptions]: ...

    @staticmethod
    def value_to_dimension(value: bool) -> Dimension2dView: ...

    def change_dimension(self, event: CheckBoxChangedEvent) -> bool: ...

    @property
    def dimension_switcher_program(self) -> Dimension2dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
