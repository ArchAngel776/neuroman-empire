from abc import ABC, abstractmethod

from lib.gui import Watcher


# Main

class Screen(Watcher, ABC):
    def __init__(self, root):
        super().__init__()
        self._root = root

    def config(self):
        pass

    @abstractmethod
    def render(self):
        pass

    @property
    def root(self):
        return self._root
