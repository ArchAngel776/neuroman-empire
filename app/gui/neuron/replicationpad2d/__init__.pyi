from lib import void
from lib.gui.element.form import FormInput
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.replicationpad2d.params import ReplicationPad2dParams
from app.network.neuron.replicationpad2d.options import ReplicationPad2dOptions
from app.network.neuron.replicationpad2d.boundary.params import ReplicationPad2dBoundaryParams
from app.network.neuron.replicationpad2d.boundary.options import ReplicationPad2dBoundaryOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Boundary2dSwitcher, Boundary2dView


# Main

class NeuronBuilderReplicationPadding2dStrategy(NeuronStrategy[ReplicationPad2dParams, ReplicationPad2dOptions]):
    class Watch(str):
        BOUNDARY_SWITCHER = ... #type: NeuronBuilderReplicationPadding2dStrategy.Watch

    _bounded: FormInput[bool]

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[ReplicationPad2dParams, ReplicationPad2dOptions]: ...

    @property
    def default_params(self) -> ReplicationPad2dParams: ...

    @property
    def default_options(self) -> ReplicationPad2dOptions: ...

    def load(self, params: ReplicationPad2dParams, options: ReplicationPad2dOptions) -> void: ...

    @property
    def boundary_params(self) -> NeuronStrategyParams[ReplicationPad2dBoundaryParams, ReplicationPad2dBoundaryOptions]: ...

    @staticmethod
    def value_to_boundary(value: bool) -> Boundary2dView: ...

    def change_boundary(self, event: CheckBoxChangedEvent) -> bool: ...

    @property
    def boundary_switcher_program(self) -> Boundary2dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
