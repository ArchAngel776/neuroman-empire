# Main

class Select2Container:
    def __init__(self):
        self._groups = []

    def add_group(self, index, group):
        self._groups.insert(index, group)
        return self

    def remove_group(self, index):
        self._groups.pop(index)
        return self

    def has(self, index):
        try:
            self[index]
        except IndexError:
            return False
        finally:
            return True

    @property
    def groups(self):
        return self._groups

    def __getitem__(self, item):
        return self._groups[item]

    def __len__(self):
        return len(self._groups)
