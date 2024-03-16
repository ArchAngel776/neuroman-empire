from lib import void
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout
from lib.gui.window import Window

from app.network.extension.reflectionpad.bounded.params import ReflectionPadBoundedParams
from app.network.extension.reflectionpad.bounded.options import ReflectionPadBoundedOptions
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies


# Main

class BoundedBoundaryStrategy(NeuronStrategy[ReflectionPadBoundedParams, ReflectionPadBoundedOptions]):
    _padding: FormInput[int]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[ReflectionPadBoundedParams, ReflectionPadBoundedOptions]: ...

    @property
    def default_params(self) -> ReflectionPadBoundedParams: ...

    @property
    def default_options(self) -> ReflectionPadBoundedOptions: ...

    def load(self, params: ReflectionPadBoundedParams, options: ReflectionPadBoundedOptions) -> void: ...

    def render(self, root: Window) -> Layout: ...
