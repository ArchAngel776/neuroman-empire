from lib import void
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout
from lib.gui.window import Window

from app.network.extension.zeropad.bounded.params import ZeroPadBoundedParams
from app.network.extension.zeropad.bounded.options import ZeroPadBoundedOptions
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies


# Main

class BoundedBoundaryStrategy(NeuronStrategy[ZeroPadBoundedParams, ZeroPadBoundedOptions]):
    _padding: FormInput[int]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[ZeroPadBoundedParams, ZeroPadBoundedOptions]: ...

    @property
    def default_params(self) -> ZeroPadBoundedParams: ...

    @property
    def default_options(self) -> ZeroPadBoundedOptions: ...

    def load(self, params: ZeroPadBoundedParams, options: ZeroPadBoundedOptions) -> void: ...

    def render(self, root: Window) -> Layout: ...
