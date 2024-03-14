from lib import void
from lib.gui.element.form import FormInput
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.adaptivemaxpool3d.params import AdaptiveMaxPool3dParams
from app.network.neuron.adaptivemaxpool3d.options import AdaptiveMaxPool3dOptions
from app.network.neuron.adaptivemaxpool3d.dimension.params import AdaptiveMaxPool3dDimensionParams
from app.network.neuron.adaptivemaxpool3d.dimension.options import AdaptiveMaxPool3dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Dimension3dView, Dimension3dSwitcher


# Main

class NeuronBuilderAdaptiveMaxPooling3dStrategy(NeuronStrategy[AdaptiveMaxPool3dParams, AdaptiveMaxPool3dOptions]):
    class Watch(str):
        DIMENSION_SWITCHER = ... #type: NeuronBuilderAdaptiveMaxPooling3dStrategy.Watch

    _return_indices: FormInput[bool]

    _reflection: FormInput[bool]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[AdaptiveMaxPool3dParams, AdaptiveMaxPool3dOptions]: ...

    @property
    def default_params(self) -> AdaptiveMaxPool3dParams: ...

    @property
    def default_options(self) -> AdaptiveMaxPool3dOptions: ...

    def load(self, params: AdaptiveMaxPool3dParams, options: AdaptiveMaxPool3dOptions) -> void: ...

    @property
    def dimension_params(self) -> NeuronStrategyParams[
        AdaptiveMaxPool3dDimensionParams, AdaptiveMaxPool3dDimensionOptions
    ]: ...

    @staticmethod
    def value_to_dimension(value: bool) -> Dimension3dView: ...

    def change_dimension(self, event: CheckBoxChangedEvent) -> bool: ...

    @property
    def dimension_switcher_program(self) -> Dimension3dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
