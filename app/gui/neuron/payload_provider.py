from lib.foundations.data_provider import DataProvider


# Main

class NeuronPayloadProvider(DataProvider):
    def __init__(self):
        super().__init__()
        self._params = None
        self._options = None

    def add(self, params, options):
        self._params = params
        self._options = options

    def provide(self):
        return self.callback

    def clear(self):
        self._params = None
        self._options = None

    def callback(self, neuron_strategy):
        if self.params is not None and self.options is not None:
            neuron_strategy.read(self.params, self.options)

    @property
    def params(self):
        return self._params

    @property
    def options(self):
        return self._options
