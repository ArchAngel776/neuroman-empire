from enum import Enum

from lib.gui.element.component.switcher.program import SwitcherProgram

from app.gui.extension.replicationpad.bounded import BoundedBoundaryStrategy
from app.gui.neuron.replicationpad2d.boundary import UnboundedBoundaryStrategy


# View

class Boundary2dView(Enum):
    BOUNDED = True
    UNBOUNDED = False


# Main

class Boundary2dSwitcher(SwitcherProgram):
    def __init__(self, key, dependencies):
        super().__init__(key, dependencies)
        self._bounded_strategy = BoundedBoundaryStrategy(dependencies)
        self._unbounded_strategy = UnboundedBoundaryStrategy(dependencies)

    @property
    def strategy(self):
        return {
            Boundary2dView.BOUNDED: self._bounded_strategy,
            Boundary2dView.UNBOUNDED: self._unbounded_strategy
        }
