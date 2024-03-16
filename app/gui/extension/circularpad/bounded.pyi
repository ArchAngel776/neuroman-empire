from lib import void
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout
from lib.gui.window import Window

from app.network.extension.circularpad.bounded.params import CircularPadBoundedParams
from app.network.extension.circularpad.bounded.options import CircularPadBoundedOptions
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies


# Main

class BoundedBoundaryStrategy(NeuronStrategy[CircularPadBoundedParams, CircularPadBoundedOptions]):
    _padding: FormInput[int]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[CircularPadBoundedParams, CircularPadBoundedOptions]: ...

    @property
    def default_params(self) -> CircularPadBoundedParams: ...

    @property
    def default_options(self) -> CircularPadBoundedOptions: ...

    def load(self, params: CircularPadBoundedParams, options: CircularPadBoundedOptions) -> void: ...

    def render(self, root: Window) -> Layout: ...
