# Main

class Select2Option:
    def __init__(self, group):
        self._group = group
        self._title = ""
        self._data = None

    def set_title(self, title):
        self._title = title
        return self

    def set_data(self, data):
        self._data = data
        return self

    @property
    def group(self):
        return self._group

    @property
    def title(self):
        return self._title

    @property
    def data(self):
        return self._data

    @property
    def index(self):
        return self._group.options.index(self)
