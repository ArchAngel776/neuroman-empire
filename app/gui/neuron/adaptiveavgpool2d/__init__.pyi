from lib import void
from lib.gui.element.form import FormInput
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.adaptiveavgpool2d.params import AdaptiveAvgPool2dParams
from app.network.neuron.adaptiveavgpool2d.options import AdaptiveAvgPool2dOptions
from app.network.neuron.adaptiveavgpool2d.dimension.params import AdaptiveAvgPool2dDimensionParams
from app.network.neuron.adaptiveavgpool2d.dimension.options import AdaptiveAvgPool2dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Dimension2dSwitcher, Dimension2dView


# Main

class NeuronBuilderAdaptiveAveragePooling2dStrategy(NeuronStrategy[AdaptiveAvgPool2dParams, AdaptiveAvgPool2dOptions]):
    class Watch(str):
        DIMENSION_SWITCHER = ... #type: NeuronBuilderAdaptiveAveragePooling2dStrategy.Watch

    _reflection: FormInput[bool]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[AdaptiveAvgPool2dParams, AdaptiveAvgPool2dOptions]: ...

    @property
    def default_params(self) -> AdaptiveAvgPool2dParams: ...

    @property
    def default_options(self) -> AdaptiveAvgPool2dOptions: ...

    def load(self, params: AdaptiveAvgPool2dParams, options: AdaptiveAvgPool2dOptions) -> void: ...

    @property
    def dimension_params(self) -> NeuronStrategyParams[
        AdaptiveAvgPool2dDimensionParams, AdaptiveAvgPool2dDimensionOptions
    ]: ...

    @staticmethod
    def value_to_dimension(value: bool) -> Dimension2dView: ...

    def change_dimension(self, event: CheckBoxChangedEvent) -> bool: ...

    @property
    def dimension_switcher_program(self) -> Dimension2dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
