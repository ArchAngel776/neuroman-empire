from typing import Union

from lib.gui.element.switcher.program import SwitcherProgram
from lib.gui.element.switcher.strategy import SwitcherStrategy

from .entry.params import NeuronEntryParams
from .creation.params import NeuronCreationParams
from .modification.params import NeuronModificationParams
from .operation import NeuronOperation
from .dependencies import NeuronOperationDependencies
from .entry import NeuronOperationEntryStrategy
from .creation import NeuronOperationCreationStrategy
from .modification import NeuronOperationModificationStrategy


# Params

NeuronOperationParams = Union[NeuronEntryParams, NeuronCreationParams, NeuronModificationParams]


# Switcher

class NeuronOperationSwitcher(SwitcherProgram[NeuronOperation, NeuronOperationDependencies, NeuronOperationParams]):
    _entry_strategy: NeuronOperationEntryStrategy
    _creation_strategy: NeuronOperationCreationStrategy
    _modification_strategy: NeuronOperationModificationStrategy

    def __init__(self, key: NeuronOperation, dependencies: NeuronOperationDependencies) -> None: ...

    @property
    def strategy(self) -> dict[NeuronOperation, SwitcherStrategy[NeuronOperationDependencies, NeuronOperationParams]]: ...
