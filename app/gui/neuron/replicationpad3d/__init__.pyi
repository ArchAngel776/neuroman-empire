from lib import void
from lib.gui.element.form import FormInput
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.replicationpad3d.params import ReplicationPad3dParams
from app.network.neuron.replicationpad3d.options import ReplicationPad3dOptions
from app.network.neuron.replicationpad3d.boundary.params import ReplicationPad3dBoundaryParams
from app.network.neuron.replicationpad3d.boundary.options import ReplicationPad3dBoundaryOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Boundary3dSwitcher, Boundary3dView


# Main

class NeuronBuilderReplicationPadding3dStrategy(NeuronStrategy[ReplicationPad3dParams, ReplicationPad3dOptions]):
    class Watch(str):
        BOUNDARY_SWITCHER = ... #type: NeuronBuilderReplicationPadding3dStrategy.Watch

    _bounded: FormInput[bool]

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[ReplicationPad3dParams, ReplicationPad3dOptions]: ...

    @property
    def default_params(self) -> ReplicationPad3dParams: ...

    @property
    def default_options(self) -> ReplicationPad3dOptions: ...

    def load(self, params: ReplicationPad3dParams, options: ReplicationPad3dOptions) -> void: ...

    @property
    def boundary_params(self) -> NeuronStrategyParams[ReplicationPad3dBoundaryParams, ReplicationPad3dBoundaryOptions]: ...

    @staticmethod
    def value_to_boundary(value: bool) -> Boundary3dView: ...

    def change_boundary(self, event: CheckBoxChangedEvent) -> bool: ...

    @property
    def boundary_switcher_program(self) -> Boundary3dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
