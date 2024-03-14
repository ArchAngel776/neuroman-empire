from lib import void
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout

from app.network.neuron.adaptivemaxpool1d.params import AdaptiveMaxPool1dParams
from app.network.neuron.adaptivemaxpool1d.options import AdaptiveMaxPool1dOptions
from app.network.neuron.adaptivemaxpool1d.dimension.params import AdaptiveMaxPool1dDimensionParams
from app.network.neuron.adaptivemaxpool1d.dimension.options import AdaptiveMaxPool1dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Dimension1dSwitcher, Dimension1dView


# Main

class NeuronBuilderAdaptiveMaxPooling1dStrategy(NeuronStrategy[AdaptiveMaxPool1dParams, AdaptiveMaxPool1dOptions]):
    class Watch(str):
        DIMENSION_SWITCHER = ... #type: NeuronBuilderAdaptiveMaxPooling1dStrategy.Watch

    _return_indices: FormInput[bool]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[AdaptiveMaxPool1dParams, AdaptiveMaxPool1dOptions]: ...

    @property
    def default_params(self) -> AdaptiveMaxPool1dParams: ...

    @property
    def default_options(self) -> AdaptiveMaxPool1dOptions: ...

    def load(self, params: AdaptiveMaxPool1dParams, options: AdaptiveMaxPool1dOptions) -> void: ...

    @property
    def dimension_params(self) -> NeuronStrategyParams[
        AdaptiveMaxPool1dDimensionParams, AdaptiveMaxPool1dDimensionOptions
    ]: ...

    @property
    def dimension_switcher_program(self) -> Dimension1dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
