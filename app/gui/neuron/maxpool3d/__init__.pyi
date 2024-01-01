from lib import void
from lib.gui.element.form import FormInput
from lib.gui.element.component.switcher import Switcher
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.maxpool3d.params import MaxPool3dParams
from app.network.neuron.maxpool3d.options import MaxPool3dOptions
from app.network.neuron.maxpool3d.dimension.params import MaxPool3dDimensionParams
from app.network.neuron.maxpool3d.dimension.options import MaxPool3dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Dimension3dView, Dimension3dSwitcher


# Main

class NeuronBuilderMaxPooling3dStrategy(NeuronStrategy[MaxPool3dParams, MaxPool3dOptions]):
    DIMENSION_SWITCHER = ... #type: str

    _return_indices: FormInput[bool]
    _ceil_mode: FormInput[bool]

    _reflection: FormInput[bool]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[MaxPool3dParams, MaxPool3dOptions]: ...

    @property
    def default_params(self) -> MaxPool3dParams: ...

    @property
    def default_options(self) -> MaxPool3dOptions: ...

    def load(self, params: MaxPool3dParams, options: MaxPool3dOptions) -> void: ...

    @property
    def dimension_params(self) -> NeuronStrategyParams[MaxPool3dDimensionParams, MaxPool3dDimensionOptions]: ...

    def change_dimension(self, event: CheckBoxChangedEvent) -> bool: ...

    @staticmethod
    def adjust_dimension_params_area(switcher: Switcher[Dimension3dView, {}, MaxPool3dDimensionParams]) -> bool: ...

    @property
    def dimension_switcher_program(self) -> Dimension3dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
