from typing import Optional

from PyQt5.QtCore import QSize, QModelIndex
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QStyledItemDelegate, QStyleOptionViewItem

from lib import void


# Main

class SelectViewDelegate(QStyledItemDelegate):
    def paint(self, painter: Optional[QPainter], option: QStyleOptionViewItem, index: QModelIndex) -> void: ...

    def sizeHint(self, option: QStyleOptionViewItem, index: QModelIndex) -> QSize: ...
