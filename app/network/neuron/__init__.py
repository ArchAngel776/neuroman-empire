from abc import ABC, abstractmethod

from app.network.neuron.type import NeuronType


# Main

class Neuron(ABC):
    def __init__(self, name, params, options):
        self._name = name
        self._params = params
        self._options = options

    @staticmethod
    @abstractmethod
    def type():
        pass

    @staticmethod
    @abstractmethod
    def title():
        pass

    @property
    def name(self):
        return self._name

    @property
    def params(self):
        return self._params

    @property
    def options(self):
        return self._options

    @staticmethod
    @abstractmethod
    def default_params():
        pass

    @staticmethod
    @abstractmethod
    def default_options():
        pass
