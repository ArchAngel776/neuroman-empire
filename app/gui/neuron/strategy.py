from abc import ABC, abstractmethod

from lib.gui.element.component.switcher.strategy import SwitcherStrategy

from app.gui.neuron.payload_provider import NeuronPayloadProvider


# Main

class NeuronStrategy(SwitcherStrategy, ABC):
    def __init__(self, dependencies):
        super().__init__(dependencies)
        self._neuron_payload_provider = NeuronPayloadProvider()

    def beforeClose(self):
        super().beforeClose()
        self.neuron_payload_provider.clear()

    @property
    @abstractmethod
    def default_params(self):
        pass

    @property
    @abstractmethod
    def default_options(self):
        pass

    @abstractmethod
    def load(self, params, options):
        pass

    def read(self, params, options):
        self.load(params, options)
        self.neuron_payload_provider.add(params, options)

    @property
    def neuron_payload_provider(self):
        return self._neuron_payload_provider
