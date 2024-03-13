from lib import void
from lib.gui.element.form import FormInput
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.avgpool3d.params import AvgPool3dParams
from app.network.neuron.avgpool3d.options import AvgPool3dOptions
from app.network.neuron.avgpool3d.dimension.params import AvgPool3dDimensionParams
from app.network.neuron.avgpool3d.dimension.options import AvgPool3dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Dimension3dView, Dimension3dSwitcher


# Main

class NeuronBuilderAveragePooling3dStrategy(NeuronStrategy[AvgPool3dParams, AvgPool3dOptions]):
    class Watch(str):
        DIMENSION_SWITCHER = ... #type: NeuronBuilderAveragePooling3dStrategy.Watch

    _ceil_mode: FormInput[bool]
    _count_include_pad: FormInput[bool]
    _divisor_override: FormInput[int]

    _reflection: FormInput[bool]
    _divisor_enabled: FormInput[bool]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[AvgPool3dParams, AvgPool3dOptions]: ...

    @property
    def default_params(self) -> AvgPool3dParams: ...

    @property
    def default_options(self) -> AvgPool3dOptions: ...

    def load(self, params: AvgPool3dParams, options: AvgPool3dOptions) -> void: ...

    @property
    def dimension_params(self) -> NeuronStrategyParams[AvgPool3dDimensionParams, AvgPool3dDimensionOptions]: ...

    @staticmethod
    def value_to_dimension(value: bool) -> Dimension3dView: ...

    def change_dimension(self, event: CheckBoxChangedEvent) -> bool: ...

    @property
    def dimension_switcher_program(self) -> Dimension3dSwitcher: ...

    def toggle_divisor(self, event: CheckBoxChangedEvent) -> bool: ...

    def update_view(self) -> void: ...

    def render(self, root: MainWindow) -> Layout: ...
