from lib.gui.element.switcher.program import SwitcherProgram

from app.gui.network.creation.params import NeuronCreationParams
from app.gui.network.modification.params import NeuronModificationParams
from app.gui.network.operation import NeuronOperation
from app.gui.network.dependencies import NeuronOperationDependencies
from app.gui.network.entry import NeuronOperationEntryStrategy
from app.gui.network.creation import NeuronOperationCreationStrategy
from app.gui.network.modification import NeuronOperationModificationStrategy


# Switcher

class NeuronOperationSwitcher(SwitcherProgram):
    def __init__(self, key, dependencies):
        super().__init__(key, dependencies)
        self._entry_strategy = NeuronOperationEntryStrategy(dependencies)
        self._creation_strategy = NeuronOperationCreationStrategy(dependencies)
        self._modification_strategy = NeuronOperationModificationStrategy(dependencies)

    @property
    def strategy(self):
        return {
            NeuronOperation.ENTRY: self._entry_strategy,
            NeuronOperation.CREATE: self._creation_strategy,
            NeuronOperation.MODIFY: self._modification_strategy
        }
