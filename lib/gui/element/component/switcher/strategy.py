from abc import abstractmethod, ABC

from lib.gui import Watcher


# Main

class SwitcherStrategy(Watcher, ABC):
    def __init__(self, dependencies):
        super().__init__()
        self._dependencies = dependencies

    def beforeShow(self):
        pass

    def afterShow(self):
        pass

    @property
    @abstractmethod
    def params(self):
        pass

    @property
    def dependencies(self):
        return self._dependencies

    @abstractmethod
    def render(self, root):
        pass

    def update_dependencies(self, dependencies):
        self._dependencies = dependencies
