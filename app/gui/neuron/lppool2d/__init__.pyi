from lib import void
from lib.gui.element.form import FormInput
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.lppool2d.params import LPPool2dParams
from app.network.neuron.lppool2d.options import LPPool2dOptions
from app.network.neuron.lppool2d.dimension.params import LPPool2dDimensionParams
from app.network.neuron.lppool2d.dimension.options import LPPool2dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Dimension2dSwitcher, Dimension2dView


# Main

class NeuronBuilderLocalPooling2dStrategy(NeuronStrategy[LPPool2dParams, LPPool2dOptions]):
    class Watch(str):
        DIMENSION_SWITCHER = ... #type: NeuronBuilderLocalPooling2dStrategy.Watch

    _power: FormInput[int]
    _ceil_mode: FormInput[bool]

    _reflection: FormInput[bool]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[LPPool2dParams, LPPool2dOptions]: ...

    @property
    def default_params(self) -> LPPool2dParams: ...

    @property
    def default_options(self) -> LPPool2dOptions: ...

    def load(self, params: LPPool2dParams, options: LPPool2dOptions) -> void: ...

    @property
    def dimension_params(self) -> NeuronStrategyParams[LPPool2dDimensionParams, LPPool2dDimensionOptions]: ...

    @staticmethod
    def value_to_dimension(value: bool) -> Dimension2dView: ...

    def change_dimension(self, event: CheckBoxChangedEvent) -> bool: ...

    @property
    def dimension_switcher_program(self) -> Dimension2dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
