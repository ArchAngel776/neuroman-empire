from lib.foundations.data_provider import DataProvider


# Main

class StringListProvider(DataProvider):
    def __init__(self):
        self._list = []

    def add(self, *data):
        self.list.extend(data)

    def provide(self):
        return self.list.pop(0)

    def clear(self):
        self.list.clear()

    @property
    def list(self):
        return self._list
