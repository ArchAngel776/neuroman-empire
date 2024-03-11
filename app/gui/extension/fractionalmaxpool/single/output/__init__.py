from lib.gui.element.component.switcher.program import SwitcherProgram

from app.network.extension.fractionalmaxpool.single.options.output import Output
from .size import OutputSizeStrategy
from .ratio import OutputRatioStrategy


# Main

class OutputSwitcher(SwitcherProgram):
    def __init__(self, key, dependencies):
        super().__init__(key, dependencies)
        self._size_strategy = OutputSizeStrategy(dependencies)
        self._ratio_strategy = OutputRatioStrategy(dependencies)

    @property
    def strategy(self):
        return {
            Output.SIZE: self._size_strategy,
            Output.RATIO: self._ratio_strategy
        }
