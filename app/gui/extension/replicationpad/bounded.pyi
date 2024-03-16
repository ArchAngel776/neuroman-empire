from lib import void
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout
from lib.gui.window import Window

from app.network.extension.replicationpad.bounded.params import ReplicationPadBoundedParams
from app.network.extension.replicationpad.bounded.options import ReplicationPadBoundedOptions
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies


# Main

class BoundedBoundaryStrategy(NeuronStrategy[ReplicationPadBoundedParams, ReplicationPadBoundedOptions]):
    _padding: FormInput[int]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[ReplicationPadBoundedParams, ReplicationPadBoundedOptions]: ...

    @property
    def default_params(self) -> ReplicationPadBoundedParams: ...

    @property
    def default_options(self) -> ReplicationPadBoundedOptions: ...

    def load(self, params: ReplicationPadBoundedParams, options: ReplicationPadBoundedOptions) -> void: ...

    def render(self, root: Window) -> Layout: ...
