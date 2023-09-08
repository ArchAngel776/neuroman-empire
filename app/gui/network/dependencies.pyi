from typing import TypedDict, Optional, Callable

from lib import void

from app.network.neuron import Neuron


# Main

class NeuronOperationDependencies(TypedDict):
    neuron: Optional[Neuron]
    create: Callable[[type[Neuron]], void]
    action_entry: Callable[[], void]
    action_creation: Callable[[], void]
