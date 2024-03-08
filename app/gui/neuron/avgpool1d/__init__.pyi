from lib import void
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout

from app.network.neuron.avgpool1d.params import AvgPool1dParams
from app.network.neuron.avgpool1d.options import AvgPool1dOptions
from app.network.neuron.avgpool1d.dimension.params import AvgPool1dDimensionParams
from app.network.neuron.avgpool1d.dimension.options import AvgPool1dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Dimension1dSwitcher, Dimension1dView


# Main

class NeuronBuilderAveragePooling1dStrategy(NeuronStrategy[AvgPool1dParams, AvgPool1dOptions]):
    class Watch(str):
        DIMENSION_SWITCHER = ... #type: NeuronBuilderAveragePooling1dStrategy.Watch

    _ceil_mode: FormInput[bool]
    _count_include_pad: FormInput[bool]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[AvgPool1dParams, AvgPool1dOptions]: ...

    @property
    def default_params(self) -> AvgPool1dParams: ...

    @property
    def default_options(self) -> AvgPool1dOptions: ...

    def load(self, params: AvgPool1dParams, options: AvgPool1dOptions) -> void: ...

    @property
    def dimension_params(self) -> NeuronStrategyParams[AvgPool1dDimensionParams, AvgPool1dDimensionOptions]: ...

    @property
    def dimension_switcher_program(self) -> Dimension1dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
