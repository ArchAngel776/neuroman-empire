from enum import Enum

from lib.gui.element.component.switcher.program import SwitcherProgram

from app.gui.extension.fractionalmaxpool.single import SingleDimensionStrategy
from app.gui.neuron.fractionalmaxpool3d.dimension import TripleDimensionStrategy


# View

class Dimension3dView(Enum):
    SINGLE = 1
    TRIPLE = 2


# Main

class Dimension3dSwitcher(SwitcherProgram):
    def __init__(self, key, dependencies):
        super().__init__(key, dependencies)
        self._single_strategy = SingleDimensionStrategy(dependencies)
        self._triple_strategy = TripleDimensionStrategy(dependencies)

    @property
    def strategy(self):
        return {
            Dimension3dView.SINGLE: self._single_strategy,
            Dimension3dView.TRIPLE: self._triple_strategy
        }