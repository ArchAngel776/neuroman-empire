from typing import TypedDict

from app.gui.neuron import NeuronParams


# Main

class NeuronCreationParams(TypedDict):
    name: str
    params: NeuronParams
