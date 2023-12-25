# Main

class DimensionRemover:
    def __init__(self, target, index):
        self._target = target
        self._index = index

    def remove(self):
        return self.target.remove_dimension(self.index)

    @property
    def target(self):
        return self._target

    @property
    def index(self):
        return self._index
