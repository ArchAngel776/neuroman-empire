from enum import Enum

from lib.gui.element.switcher.program import SwitcherProgram

from app.gui.neuron.maxpool1d.dimension import SingleDimensionStrategy
from app.gui.neuron.maxpool3d.dimension import TripleDimensionStrategy


# View

class Dimension3dView(Enum):
    SINGLE = 1
    TRIPLE = 3


# Main

class Dimension3dSwitcher(SwitcherProgram):
    def __init__(self, key):
        super().__init__(key, {})
        self._single_strategy = SingleDimensionStrategy()
        self._triple_strategy = TripleDimensionStrategy()

    @property
    def strategy(self):
        return {
            Dimension3dView.SINGLE: self._single_strategy,
            Dimension3dView.TRIPLE: self._triple_strategy
        }
