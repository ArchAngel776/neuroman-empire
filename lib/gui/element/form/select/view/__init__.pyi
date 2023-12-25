from PyQt5.QtCore import QPoint, QModelIndex, QRect
from PyQt5.QtGui import QPaintEvent
from PyQt5.QtWidgets import QAbstractItemView

from lib import void
from lib.gui.element.form.select import SelectBox


# Main

class SelectView(QAbstractItemView):
    def __init__(self, parent: SelectBox) -> None: ...

    def indexAt(self, point: QPoint) -> QModelIndex: ...

    def paintEvent(self, event: QPaintEvent) -> void: ...

    def horizontalOffset(self) -> int: ...

    def verticalOffset(self) -> int: ...

    def visualRect(self, index: QModelIndex) -> QRect: ...

    def scrollTo(
            self,
            index: QModelIndex,
            hint: QAbstractItemView.ScrollHint = QAbstractItemView.ScrollHint.EnsureVisible
    ) -> void: ...
