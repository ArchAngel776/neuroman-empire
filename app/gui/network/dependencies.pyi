from typing import TypedDict, Optional, Callable

from lib import void

from app.network import Network
from app.network.neuron import Neuron


# Main

class NeuronOperationDependencies(TypedDict):
    network: Network
    neuron: Optional[Neuron]
    create: Callable[[type[Neuron]], void]
    remove: Callable[[Neuron], void]
    action_entry: Callable[[], void]
    action_creation: Callable[[], void]
