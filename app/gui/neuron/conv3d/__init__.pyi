from lib import void
from lib.gui.element.form import FormInput
from lib.gui.element.component.switcher import Switcher
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.conv3d.params import Conv3dParams
from app.network.neuron.conv3d.options import Conv3dOptions
from app.network.neuron.conv3d.dimension.params import Conv3dDimensionParams
from app.network.neuron.conv3d.dimension.options import Conv3dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Dimension3dView, Dimension3dSwitcher


# Main

class NeuronBuilderConvolution3dStrategy(NeuronStrategy[Conv3dParams, Conv3dOptions]):
    class Watch(str):
        DIMENSION_SWITCHER = ... #type: NeuronBuilderConvolution3dStrategy.Watch

    _input_channels: FormInput[int]
    _output_channels: FormInput[int]
    _groups: FormInput[int]
    _bias: FormInput[bool]

    _reflection: FormInput[bool]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[Conv3dParams, Conv3dOptions]: ...

    @property
    def default_params(self) -> Conv3dParams: ...

    @property
    def default_options(self) -> Conv3dOptions: ...

    def load(self, params: Conv3dParams, options: Conv3dOptions) -> void: ...

    @property
    def dimension_params(self) -> NeuronStrategyParams[Conv3dDimensionParams, Conv3dDimensionOptions]: ...

    @staticmethod
    def value_to_dimension(value: bool) -> Dimension3dView: ...

    def change_dimension(self, event: CheckBoxChangedEvent) -> bool: ...

    @property
    def dimension_switcher_program(self) -> Dimension3dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
