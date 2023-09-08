from lib.gui.element.form import FormInput
from lib.gui.element.switcher import Switcher
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.conv3d.params import Conv3dParams
from app.network.neuron.conv3d.options import Conv3dOptions
from app.network.neuron.conv3d.dimension.params import Conv3dDimensionParams
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy

from .view import Dimension3dView, Dimension3dSwitcher
from .dependencies import Convolution3dStrategyDependencies
from .dimension.dependencies import TripleDimensionStrategyDependencies


# Main

class NeuronBuilderConvolution3dStrategy(
    NeuronStrategy[Convolution3dStrategyDependencies, Conv3dParams, Conv3dOptions]
):
    DIMENSION_SWITCHER = ... #type: str

    _input_channels: FormInput[int]
    _output_channels: FormInput[int]
    _groups: FormInput[int]
    _bias: FormInput[bool]

    _reflection: FormInput[bool]

    _input_height: int

    def __init__(self, dependencies: Convolution3dStrategyDependencies) -> None: ...

    @property
    def params(self) -> Conv3dParams: ...

    @property
    def default_params(self) -> Conv3dParams: ...

    @property
    def default_options(self) -> Conv3dOptions: ...

    @property
    def dimension_params(self) -> Conv3dDimensionParams: ...

    def change_dimension(self, event: CheckBoxChangedEvent) -> bool: ...

    @staticmethod
    def adjust_dimension_params_area(
            switcher: Switcher[Dimension3dView, TripleDimensionStrategyDependencies, Conv3dDimensionParams]
    ) -> bool: ...

    @property
    def dimension_switcher_program(self) -> Dimension3dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
