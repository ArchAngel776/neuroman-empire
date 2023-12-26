from enum import Enum

from lib.gui.element.switcher.program import SwitcherProgram

from app.gui.neuron.convtranspose1d.dimension import SingleDimensionStrategy
from app.gui.neuron.convtranspose2d.dimension import DoubleDimensionStrategy


# View

class Dimension2dView(Enum):
    SINGLE = 1
    DOUBLE = 2


# Main

class Dimension2dSwitcher(SwitcherProgram):
    def __init__(self, key, dependencies):
        super().__init__(key, dependencies)
        self._single_strategy = SingleDimensionStrategy(dependencies)
        self._double_strategy = DoubleDimensionStrategy(dependencies)

    @property
    def strategy(self):
        return {
            Dimension2dView.SINGLE: self._single_strategy,
            Dimension2dView.DOUBLE: self._double_strategy
        }
