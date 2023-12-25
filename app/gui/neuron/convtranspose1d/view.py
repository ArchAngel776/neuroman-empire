from enum import Enum

from lib.gui.element.switcher.program import SwitcherProgram

from app.gui.neuron.convtranspose1d.dimension import SingleDimensionStrategy


# View

class Dimension1dView(Enum):
    SINGLE = 1


# Main

class Dimension1dSwitcher(SwitcherProgram):
    def __init__(self, key):
        super().__init__(key, {})
        self._single_strategy = SingleDimensionStrategy()

    @property
    def strategy(self):
        return {
            Dimension1dView.SINGLE: self._single_strategy
        }
