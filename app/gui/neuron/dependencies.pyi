from typing import TypedDict

from app.network import Network


# Main

class NeuronBuilderDependencies(TypedDict):
    network: Network
