from lib import void
from lib.gui.element.form import FormInput
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.replicationpad1d.params import ReplicationPad1dParams
from app.network.neuron.replicationpad1d.options import ReplicationPad1dOptions
from app.network.neuron.replicationpad1d.boundary.params import ReplicationPad1dBoundaryParams
from app.network.neuron.replicationpad1d.boundary.options import ReplicationPad1dBoundaryOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Boundary1dSwitcher, Boundary1dView


# Main

class NeuronBuilderReplicationPadding1dStrategy(NeuronStrategy[ReplicationPad1dParams, ReplicationPad1dOptions]):
    class Watch(str):
        BOUNDARY_SWITCHER = ... #type: NeuronBuilderReplicationPadding1dStrategy.Watch

    _bounded: FormInput[bool]

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[ReplicationPad1dParams, ReplicationPad1dOptions]: ...

    @property
    def default_params(self) -> ReplicationPad1dParams: ...

    @property
    def default_options(self) -> ReplicationPad1dOptions: ...

    def load(self, params: ReplicationPad1dParams, options: ReplicationPad1dOptions) -> void: ...

    @property
    def boundary_params(self) -> NeuronStrategyParams[ReplicationPad1dBoundaryParams, ReplicationPad1dBoundaryOptions]: ...

    @staticmethod
    def value_to_boundary(value: bool) -> Boundary1dView: ...

    def change_boundary(self, event: CheckBoxChangedEvent) -> bool: ...

    @property
    def boundary_switcher_program(self) -> Boundary1dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
