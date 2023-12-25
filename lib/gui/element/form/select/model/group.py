class SelectModelGroup:
    def __init__(self):
        self._name = ""
        self._items = []

    def setName(self, name):
        self._name = name
        return self

    def add(self, title, data=None):
        self._items.append((title, data))
        return self

    @property
    def name(self):
        return self._name

    def __getitem__(self, index):
        if index in range(0, len(self)):
            return self._items[index]
        raise IndexError

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        index = 0
        while index < len(self):
            yield self[index]
            index += 1
