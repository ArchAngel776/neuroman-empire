from lib import void
from lib.gui.element.form import FormInput
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.fractionalmaxpool2d.params import FractionalMaxPool2dParams
from app.network.neuron.fractionalmaxpool2d.options import FractionalMaxPool2dOptions
from app.network.neuron.fractionalmaxpool2d.dimension.params import FractionalMaxPool2dDimensionParams
from app.network.neuron.fractionalmaxpool2d.dimension.options import FractionalMaxPool2dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Dimension2dSwitcher, Dimension2dView


# Main

class NeuronBuilderFractionalMaxPooling2dStrategy(NeuronStrategy[FractionalMaxPool2dParams, FractionalMaxPool2dOptions]):
    class Watch(str):
        DIMENSION_SWITCHER = ... #type: NeuronBuilderFractionalMaxPooling2dStrategy.Watch

    _return_indices: FormInput[bool]

    _reflection: FormInput[bool]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[FractionalMaxPool2dParams, FractionalMaxPool2dOptions]: ...

    @property
    def default_params(self) -> FractionalMaxPool2dParams: ...

    @property
    def default_options(self) -> FractionalMaxPool2dOptions: ...

    def load(self, params: FractionalMaxPool2dParams, options: FractionalMaxPool2dOptions) -> void: ...

    @property
    def dimension_params(self) -> NeuronStrategyParams[
        FractionalMaxPool2dDimensionParams, FractionalMaxPool2dDimensionOptions
    ]: ...

    @staticmethod
    def value_to_dimension(value: bool) -> Dimension2dView: ...

    def change_dimension(self, event: CheckBoxChangedEvent) -> bool: ...

    @property
    def dimension_switcher_program(self) -> Dimension2dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
