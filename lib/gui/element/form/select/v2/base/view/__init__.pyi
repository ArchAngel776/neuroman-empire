from typing import Generic, TypeVar, ClassVar

from PyQt5.QtCore import QModelIndex, pyqtSignal
from PyQt5.QtWidgets import QTreeView

from lib import void
from lib.gui.element.form.select.v2 import Select2Box

# Types

Select2ViewData = TypeVar("Select2ViewData")


# Main

class Select2View(QTreeView, Generic[Select2ViewData]):
    # Signals

    currentIndexChanged: ClassVar[pyqtSignal] = ...

    def __init__(self, parent: Select2Box[Select2ViewData]) -> None: ...

    def setCurrentIndex(self, index: QModelIndex) -> void: ...

    # Slots

    def toggleGroup(self, index: QModelIndex) -> void: ...

    def expandCurrentGroup(self, index: QModelIndex) -> void: ...

    def adjustContentFrame(self) -> void: ...

    def closeTheRest(self, index: QModelIndex) -> void: ...
