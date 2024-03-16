from enum import Enum

from lib.gui.element.component.switcher.program import SwitcherProgram

from app.gui.extension.reflectionpad.bounded import BoundedBoundaryStrategy
from app.gui.neuron.reflectionpad3d.boundary import UnboundedBoundaryStrategy


# View

class Boundary3dView(Enum):
    BOUNDED = True
    UNBOUNDED = False


# Main

class Boundary3dSwitcher(SwitcherProgram):
    def __init__(self, key, dependencies):
        super().__init__(key, dependencies)
        self._bounded_strategy = BoundedBoundaryStrategy(dependencies)
        self._unbounded_strategy = UnboundedBoundaryStrategy(dependencies)

    @property
    def strategy(self):
        return {
            Boundary3dView.BOUNDED: self._bounded_strategy,
            Boundary3dView.UNBOUNDED: self._unbounded_strategy
        }
