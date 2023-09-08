from lib.gui.element.form import FormInput
from lib.gui.layout import Layout

from app.network.neuron.linear.params import LinearParams
from app.network.neuron.linear.options import LinearOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy

from .dependencies import LinearStrategyDependencies


# Main

class NeuronBuilderLinearStrategy(NeuronStrategy[LinearStrategyDependencies, LinearParams, LinearOptions]):
    _input_features: FormInput[int]
    _output_features: FormInput[int]
    _bias: FormInput[bool]

    _input_height: int

    def __init__(self, dependencies: LinearStrategyDependencies) -> None: ...

    @property
    def params(self) -> LinearParams: ...

    @property
    def default_params(self) -> LinearParams: ...

    @property
    def default_options(self) -> LinearOptions: ...

    def render(self, root: MainWindow) -> Layout: ...
