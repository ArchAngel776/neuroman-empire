from typing import TypedDict

from app.gui.neuron import NeuronParams, NeuronOptions


# Main

class NeuronCreationParams(TypedDict):
    name: str
    params: NeuronParams
    options: NeuronOptions
