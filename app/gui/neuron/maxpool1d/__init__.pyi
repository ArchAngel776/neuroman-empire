from lib import void
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout

from app.network.neuron.maxpool1d.params import MaxPool1dParams
from app.network.neuron.maxpool1d.options import MaxPool1dOptions
from app.network.neuron.maxpool1d.dimension.params import MaxPool1dDimensionParams
from app.network.neuron.maxpool1d.dimension.options import MaxPool1dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Dimension1dSwitcher, Dimension1dView


# Main

class NeuronBuilderMaxPooling1dStrategy(NeuronStrategy[MaxPool1dParams, MaxPool1dOptions]):
    DIMENSION_SWITCHER = ... #type: str

    _return_indices: FormInput[bool]
    _ceil_mode: FormInput[bool]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[MaxPool1dParams, MaxPool1dOptions]: ...

    @property
    def default_params(self) -> MaxPool1dParams: ...

    @property
    def default_options(self) -> MaxPool1dOptions: ...

    def load(self, params: MaxPool1dParams, options: MaxPool1dOptions) -> void: ...

    @property
    def dimension_params(self) -> NeuronStrategyParams[MaxPool1dDimensionParams, MaxPool1dDimensionOptions]: ...

    @property
    def dimension_switcher_program(self) -> Dimension1dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
