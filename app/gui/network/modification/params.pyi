from typing import TypedDict

from app.gui.neuron import NeuronParams


# Main

class NeuronModificationParams(TypedDict):
    name: str
    params: NeuronParams
