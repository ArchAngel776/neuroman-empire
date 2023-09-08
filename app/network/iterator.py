# Main

class NetworkIterator:
    def __init__(self, network):
        self._network = network
        self._index = 0

    def __next__(self):
        if self._index >= len(self._network):
            raise StopIteration

        result = self._network[self._index]
        self._index += 1
        return result
