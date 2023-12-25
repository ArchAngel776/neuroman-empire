from lib import void
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout

from app.network.neuron.linear.params import LinearParams
from app.network.neuron.linear.options import LinearOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams


# Main

class NeuronBuilderLinearStrategy(NeuronStrategy[LinearParams, LinearOptions]):
    _input_features: FormInput[int]
    _output_features: FormInput[int]
    _bias: FormInput[bool]

    _input_height: int

    def __init__(self) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[LinearParams, LinearOptions]: ...

    @property
    def default_params(self) -> LinearParams: ...

    @property
    def default_options(self) -> LinearOptions: ...

    def load(self, params: LinearParams, options: LinearOptions) -> void: ...

    def render(self, root: MainWindow) -> Layout: ...
