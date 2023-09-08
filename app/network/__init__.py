from app.network.neuron import Neuron


# Main

class Network:
    def __init__(self, neurons):
        self._neurons = neurons

    def add_neuron(self, neuron):
        self._neurons.append(neuron)
        return self

    @property
    def neurons(self):
        return self._neurons

    def __getitem__(self, index):
        return self._neurons[index]

    def __len__(self):
        return len(self._neurons)

    def __iter__(self):
        index = 0
        while index < len(self):
            yield self[index]
            index += 1
