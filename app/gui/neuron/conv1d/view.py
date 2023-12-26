from enum import Enum

from lib.gui.element.switcher.program import SwitcherProgram

from app.gui.neuron.conv1d.dimension import SingleDimensionStrategy


# View

class Dimension1dView(Enum):
    SINGLE = 1


# Main

class Dimension1dSwitcher(SwitcherProgram):
    def __init__(self, key, dependencies):
        super().__init__(key, dependencies)
        self._single_strategy = SingleDimensionStrategy(dependencies)

    @property
    def strategy(self):
        return {
            Dimension1dView.SINGLE: self._single_strategy
        }
