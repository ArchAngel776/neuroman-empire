from typing import Any

from PyQt5.QtCore import QAbstractItemModel, Qt, QModelIndex

from lib.gui.element.form.select.model.group import SelectModelGroup


# Main

class SelectModel(QAbstractItemModel):
    def __init__(self, parent):
        super().__init__(parent)
        self._groups = []

    def index(self, row, column, parent=QModelIndex()):
        return self.createIndex(row, column)

    def parent(self, child):
        return QModelIndex()

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemFlag.ItemIsEnabled
        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEditable

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        return self.groups[index.row()].name

    def rowCount(self, parent=QModelIndex()):
        return len(self.groups)

    def columnCount(self, parent=QModelIndex):
        return 1

    def setData(self, index, value, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return False

        self.groups[index.row()].setName(value)

        self.dataChanged.emit(index, index, [role])
        return True

    def insertRows(self, row, count, parent=QModelIndex()):
        self.beginInsertRows(parent, row, row + count - 1)

        for i in range(count):
            self.groups.insert(row, SelectModelGroup())

        self.endInsertRows()
        return True

    def removeRows(self, row, count, parent=QModelIndex()):
        self.beginRemoveRows(parent, row, row + count - 1)

        for i in range(count):
            self.groups.pop(row)

        self.endRemoveRows()
        return True

    @property
    def groups(self):
        return self._groups
