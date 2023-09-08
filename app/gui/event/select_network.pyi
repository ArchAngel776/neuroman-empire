from lib.gui.event.select_box_selected import SelectBoxSelectedEvent

from app.network.neuron import Neuron


# Main

class SelectNeuronEvent(SelectBoxSelectedEvent[type[Neuron]]):
    pass
