from lib import void
from lib.gui.element.form import FormInput
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.adaptiveavgpool3d.params import AdaptiveAvgPool3dParams
from app.network.neuron.adaptiveavgpool3d.options import AdaptiveAvgPool3dOptions
from app.network.neuron.adaptiveavgpool3d.dimension.params import AdaptiveAvgPool3dDimensionParams
from app.network.neuron.adaptiveavgpool3d.dimension.options import AdaptiveAvgPool3dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Dimension3dView, Dimension3dSwitcher


# Main

class NeuronBuilderAdaptiveAveragePooling3dStrategy(NeuronStrategy[AdaptiveAvgPool3dParams, AdaptiveAvgPool3dOptions]):
    class Watch(str):
        DIMENSION_SWITCHER = ... #type: NeuronBuilderAdaptiveAveragePooling3dStrategy.Watch

    _reflection: FormInput[bool]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[AdaptiveAvgPool3dParams, AdaptiveAvgPool3dOptions]: ...

    @property
    def default_params(self) -> AdaptiveAvgPool3dParams: ...

    @property
    def default_options(self) -> AdaptiveAvgPool3dOptions: ...

    def load(self, params: AdaptiveAvgPool3dParams, options: AdaptiveAvgPool3dOptions) -> void: ...

    @property
    def dimension_params(self) -> NeuronStrategyParams[
        AdaptiveAvgPool3dDimensionParams, AdaptiveAvgPool3dDimensionOptions
    ]: ...

    @staticmethod
    def value_to_dimension(value: bool) -> Dimension3dView: ...

    def change_dimension(self, event: CheckBoxChangedEvent) -> bool: ...

    @property
    def dimension_switcher_program(self) -> Dimension3dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
