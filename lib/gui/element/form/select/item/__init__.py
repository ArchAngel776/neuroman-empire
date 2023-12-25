class SelectItem:
    def __init__(self, item_type, data=None):
        self._item_type = item_type
        self._data = data

    @property
    def item_type(self):
        return self._item_type

    @property
    def data(self):
        return self._data
