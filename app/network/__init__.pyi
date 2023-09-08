from typing import TypeVar, Iterator

from .neuron import Neuron

# Types

TNetwork = TypeVar("TNetwork", bound=Network)


# Main

class Network:
    _neurons: list[Neuron]

    def __init__(self, neurons: list[Neuron]) -> None: ...

    def add_neuron(self: TNetwork, neuron: Neuron) -> TNetwork: ...

    @property
    def neurons(self) -> list[Neuron]: ...

    def __getitem__(self, index) -> Neuron: ...

    def __len__(self) -> int: ...

    def __iter__(self) -> Iterator[Neuron]: ...
