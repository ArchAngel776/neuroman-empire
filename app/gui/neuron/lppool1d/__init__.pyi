from lib import void
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout

from app.network.neuron.lppool1d.params import LPPool1dParams
from app.network.neuron.lppool1d.options import LPPool1dOptions
from app.network.neuron.lppool1d.dimension.params import LPPool1dDimensionParams
from app.network.neuron.lppool1d.dimension.options import LPPool1dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Dimension1dSwitcher, Dimension1dView


# Main

class NeuronBuilderLocalPooling1dStrategy(NeuronStrategy[LPPool1dParams, LPPool1dOptions]):
    class Watch(str):
        DIMENSION_SWITCHER = ... #type: NeuronBuilderLocalPooling1dStrategy.Watch

    _power: FormInput[int]
    _ceil_mode: FormInput[bool]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[LPPool1dParams, LPPool1dOptions]: ...

    @property
    def default_params(self) -> LPPool1dParams: ...

    @property
    def default_options(self) -> LPPool1dOptions: ...

    def load(self, params: LPPool1dParams, options: LPPool1dOptions) -> void: ...

    @property
    def dimension_params(self) -> NeuronStrategyParams[LPPool1dDimensionParams, LPPool1dDimensionOptions]: ...

    @property
    def dimension_switcher_program(self) -> Dimension1dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
