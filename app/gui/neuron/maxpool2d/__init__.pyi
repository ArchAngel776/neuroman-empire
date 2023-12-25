from lib import void
from lib.gui.element.form import FormInput
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.maxpool2d.params import MaxPool2dParams
from app.network.neuron.maxpool2d.options import MaxPool2dOptions
from app.network.neuron.maxpool2d.dimension.params import MaxPool2dDimensionParams
from app.network.neuron.maxpool2d.dimension.options import MaxPool2dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams

from .view import Dimension2dSwitcher


# Main

class NeuronBuilderMaxPooling2dStrategy(NeuronStrategy[MaxPool2dParams, MaxPool2dOptions]):
    DIMENSION_SWITCHER = ... #type: str

    _return_indices: FormInput[bool]
    _ceil_mode: FormInput[bool]

    _reflection: FormInput[bool]

    _input_height: int

    def __init__(self) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[MaxPool2dParams, MaxPool2dOptions]: ...

    @property
    def default_params(self) -> MaxPool2dParams: ...

    @property
    def default_options(self) -> MaxPool2dOptions: ...

    def load(self, params: MaxPool2dParams, options: MaxPool2dOptions) -> void: ...

    @property
    def dimension_params(self) -> NeuronStrategyParams[MaxPool2dDimensionParams, MaxPool2dDimensionOptions]: ...

    def change_dimension(self, event: CheckBoxChangedEvent) -> bool: ...

    @property
    def dimension_switcher_program(self) -> Dimension2dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
