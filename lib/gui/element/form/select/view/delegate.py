from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QStyledItemDelegate


# Main

class SelectViewDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        pass

    def sizeHint(self, option, index):
        return QSize(237, 17)
