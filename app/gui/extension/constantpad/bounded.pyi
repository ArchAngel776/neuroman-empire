from lib import void
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout
from lib.gui.window import Window

from app.network.extension.constantpad.bounded.params import ConstantPadBoundedParams
from app.network.extension.constantpad.bounded.options import ConstantPadBoundedOptions
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies


# Main

class BoundedBoundaryStrategy(NeuronStrategy[ConstantPadBoundedParams, ConstantPadBoundedOptions]):
    _padding: FormInput[int]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[ConstantPadBoundedParams, ConstantPadBoundedOptions]: ...

    @property
    def default_params(self) -> ConstantPadBoundedParams: ...

    @property
    def default_options(self) -> ConstantPadBoundedOptions: ...

    def load(self, params: ConstantPadBoundedParams, options: ConstantPadBoundedOptions) -> void: ...

    def render(self, root: Window) -> Layout: ...
