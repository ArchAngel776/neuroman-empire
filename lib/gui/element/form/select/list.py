from PyQt5.QtCore import QRect, QSize, QModelIndex, Qt, QObject
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QListView, QStyledItemDelegate, QStyleOptionViewItem


class Delegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        super().paint(painter, option, index)
        # print("Paint: ", option)

    def sizeHint(self, option, index):
        hint = super().sizeHint(option, index)
        return QSize(hint.width(), hint.height())


class List(QListView):
    def __init__(self, parent):
        super().__init__(parent)
        self.setItemDelegate(Delegate(self))
        # self.setItemDelegate(None)

    def indexAt(self, p):
        return QModelIndex()

    def paintEvent(self, e):
        # super().paintEvent(e)

        if not self.itemDelegate():
            return

        option: QStyleOptionViewItem = self.viewOptions()
        painter: QPainter = QPainter(self.viewport())

        # e.rect().translated(self.horizontalOffset(), self.verticalOffset())

    def visualRect(self, index):
        # print("Index: ", f"{index.row()}: {index.data(Qt.ItemDataRole.DisplayRole)}")
        return super().visualRect(index)
