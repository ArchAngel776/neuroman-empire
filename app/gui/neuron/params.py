# Main

class NeuronStrategyParams:
    def __init__(self, params, options):
        self._params = params
        self._options = options

    @property
    def params(self):
        return self._params

    @property
    def options(self):
        return self._options
