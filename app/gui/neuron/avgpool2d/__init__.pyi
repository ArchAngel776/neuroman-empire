from lib import void
from lib.gui.element.form import FormInput
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.avgpool2d.params import AvgPool2dParams
from app.network.neuron.avgpool2d.options import AvgPool2dOptions
from app.network.neuron.avgpool2d.dimension.params import AvgPool2dDimensionParams
from app.network.neuron.avgpool2d.dimension.options import AvgPool2dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Dimension2dSwitcher


# Main

class NeuronBuilderAveragePooling2dStrategy(NeuronStrategy[AvgPool2dParams, AvgPool2dOptions]):
    class Watch(str):
        DIMENSION_SWITCHER = ... #type: NeuronBuilderAveragePooling2dStrategy.Watch

    _ceil_mode: FormInput[bool]
    _count_include_pad: FormInput[bool]
    _divisor_override: FormInput[int]

    _reflection: FormInput[bool]
    _divisor_enabled: FormInput[bool]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[AvgPool2dParams, AvgPool2dOptions]: ...

    @property
    def default_params(self) -> AvgPool2dParams: ...

    @property
    def default_options(self) -> AvgPool2dOptions: ...

    def load(self, params: AvgPool2dParams, options: AvgPool2dOptions) -> void: ...

    @property
    def dimension_params(self) -> NeuronStrategyParams[AvgPool2dDimensionParams, AvgPool2dDimensionOptions]: ...

    def change_dimension(self, event: CheckBoxChangedEvent) -> bool: ...

    @property
    def dimension_switcher_program(self) -> Dimension2dSwitcher: ...

    def toggle_divisor(self, event: CheckBoxChangedEvent) -> bool: ...

    def update_view(self) -> void: ...

    def render(self, root: MainWindow) -> Layout: ...
