from lib import void
from lib.gui.element.form import FormInput
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.adaptivemaxpool2d.params import AdaptiveMaxPool2dParams
from app.network.neuron.adaptivemaxpool2d.options import AdaptiveMaxPool2dOptions
from app.network.neuron.adaptivemaxpool2d.dimension.params import AdaptiveMaxPool2dDimensionParams
from app.network.neuron.adaptivemaxpool2d.dimension.options import AdaptiveMaxPool2dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Dimension2dSwitcher, Dimension2dView


# Main

class NeuronBuilderAdaptiveMaxPooling2dStrategy(NeuronStrategy[AdaptiveMaxPool2dParams, AdaptiveMaxPool2dOptions]):
    class Watch(str):
        DIMENSION_SWITCHER = ... #type: NeuronBuilderAdaptiveMaxPooling2dStrategy.Watch

    _return_indices: FormInput[bool]

    _reflection: FormInput[bool]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[AdaptiveMaxPool2dParams, AdaptiveMaxPool2dOptions]: ...

    @property
    def default_params(self) -> AdaptiveMaxPool2dParams: ...

    @property
    def default_options(self) -> AdaptiveMaxPool2dOptions: ...

    def load(self, params: AdaptiveMaxPool2dParams, options: AdaptiveMaxPool2dOptions) -> void: ...

    @property
    def dimension_params(self) -> NeuronStrategyParams[
        AdaptiveMaxPool2dDimensionParams, AdaptiveMaxPool2dDimensionOptions
    ]: ...

    @staticmethod
    def value_to_dimension(value: bool) -> Dimension2dView: ...

    def change_dimension(self, event: CheckBoxChangedEvent) -> bool: ...

    @property
    def dimension_switcher_program(self) -> Dimension2dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
