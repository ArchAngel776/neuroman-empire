from app.network import Network
from app.network.neuron import Neuron


# Main

class NetworkIterator:
    _network: Network
    _index: int

    def __init__(self, network: Network) -> None: ...

    def __next__(self) -> Neuron: ...
