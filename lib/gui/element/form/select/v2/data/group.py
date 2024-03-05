# Main

class Select2Group:
    def __init__(self, container, group_id):
        self._container = container
        self._group_id = group_id
        self._name = ""
        self._options = []

    def set_group_id(self, group_id):
        self._group_id = group_id
        return self

    def set_name(self, name):
        self._name = name
        return self

    def add_option(self, index, option):
        self._options.insert(index, option)
        return self

    def remove_option(self, index):
        self._options.pop(index)
        return self

    def has(self, index):
        try:
            self[index]
        except IndexError:
            return False
        finally:
            return True

    @property
    def container(self):
        return self._container

    @property
    def group_id(self):
        return self._group_id

    @property
    def name(self):
        return self._name

    @property
    def options(self):
        return self._options

    @property
    def index(self):
        return self._container.groups.index(self)

    def __getitem__(self, item):
        return self._options[item]

    def __len__(self):
        return len(self._options)
