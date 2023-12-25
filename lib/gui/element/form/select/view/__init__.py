from PyQt5.QtCore import QModelIndex, QRect
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QAbstractItemView, QStyleOptionViewItem

from lib.gui.element.form.select.view.delegate import SelectViewDelegate


# Main

class SelectView(QAbstractItemView):
    def __init__(self, parent):
        super().__init__(parent)
        self.setItemDelegate(SelectViewDelegate(self))

    def indexAt(self, point):
        return QModelIndex()

    def paintEvent(self, event):
        super().paintEvent(event)

    def horizontalOffset(self):
        return 0

    def verticalOffset(self):
        return 0

    def visualRect(self, index):
        hint = self.itemDelegate().sizeHint(QStyleOptionViewItem(), index)

        if not hint.isValid():
            return QRect()

        return QRect(
            -self.horizontalOffset(), index.row() * hint.height() - self.verticalOffset(),
            hint.width(), hint.height()
        )

    def scrollTo(self, index, hint=QAbstractItemView.ScrollHint.EnsureVisible):
        pass
