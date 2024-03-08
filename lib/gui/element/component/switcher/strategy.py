from abc import abstractmethod, ABC

from PyQt5.QtCore import pyqtSignal

from lib.foundations import Foundation
from lib.gui import Watcher


# Meta

class SwitcherStrategyMeta(type(Foundation), type(ABC)):
    pass


# Main

class SwitcherStrategy(Foundation, Watcher, ABC, metaclass=SwitcherStrategyMeta):
    # Signal

    view_updated = pyqtSignal()

    def __init__(self, dependencies):
        Foundation.__init__(self)
        Watcher.__init__(self)
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

    def update_view(self):
        self.view_updated.emit()

    def update_dependencies(self, dependencies):
        self._dependencies = dependencies
