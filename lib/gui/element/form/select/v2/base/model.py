from PyQt5.QtCore import QAbstractItemModel, QModelIndex, Qt
from PyQt5.QtGui import QBrush

from lib.gui.element.font import Font
from lib.hooks import index_of, is_index
from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.element.form.select.v2.data import Select2Container
from lib.gui.element.form.select.v2.data.group import Select2Group
from lib.gui.element.form.select.v2.data.option import Select2Option


# Decorators

class UpdateData(Decorator):
    def method(self, target, index, value, role=Qt.ItemDataRole.DisplayRole):
        result = super().method(target, index, value, role)
        if result:
            target.dataChanged.emit(index, index, [role])
        return result


class InsertCycle(Decorator):
    def method(self, target, row, count, parent=QModelIndex()):
        target.beginInsertRows(parent, row, row + count - 1)
        result = super().method(target, row, count, parent)
        target.endInsertRows()
        return result


class RemoveCycle(Decorator):
    def method(self, target, row, count, parent=QModelIndex()):
        target.beginRemoveRows(parent, row, row + count - 1)
        result = super().method(target, row, count, parent)
        target.endRemoveRows()
        return result


# Main

class Select2Model(QAbstractItemModel):
    def __init__(self, parent, group_id_provider):
        super().__init__(parent)
        self._container = Select2Container()
        self._group_id_provider = group_id_provider

    @staticmethod
    def item_type(index):
        if index.isValid():
            if isinstance(index.internalPointer(), Select2Group):
                return Select2Group
            elif isinstance(index.internalPointer(), Select2Option):
                return Select2Option
            else:
                raise TypeError("Specified index is a valid QModelIndex but can't be used in this model type.")

        return Select2Container

    def index(self, row, column, parent=QModelIndex()):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        match self.item_type(parent).__name__:
            case Select2Container.__name__:
                if self.container.has(row):
                    return self.createIndex(row, column, self.container[row])
            case Select2Group.__name__:
                item = index_of(parent, Select2Group)
                if item.has(row):
                    return self.createIndex(row, column, item[row])

        return QModelIndex()

    def parent(self, child=QModelIndex()):
        if child.isValid() and issubclass(self.item_type(child), Select2Option):
            item = index_of(child, Select2Option).group
            return self.createIndex(item.index, 0, item)

        return QModelIndex()

    def flags(self, index):
        flags = Qt.ItemFlag.ItemIsEnabled

        if index.isValid():
            flags |= Qt.ItemFlag.ItemIsEditable

        if is_index(index, Select2Option):
            flags |= Qt.ItemFlag.ItemIsSelectable

        return flags

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        match self.item_type(index).__name__:
            case Select2Group.__name__:
                match role:
                    case Qt.ItemDataRole.DisplayRole:
                        return index_of(index, Select2Group).name

            case Select2Option.__name__:
                match role:
                    case Qt.ItemDataRole.DisplayRole:
                        return index_of(index, Select2Option).title
                    case Qt.ItemDataRole.UserRole:
                        return index_of(index, Select2Option).data

        return None

    def rowCount(self, parent=QModelIndex()):
        if not parent.isValid():
            return len(self.container)

        elif issubclass(self.item_type(parent), Select2Group):
            return len(index_of(parent, Select2Group))

        return 0

    def columnCount(self, parent=QModelIndex()):
        return 1

    @method(UpdateData)
    def setData(self, index, value, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return False

        match self.item_type(index).__name__:
            case Select2Group.__name__:
                if role == Qt.ItemDataRole.DisplayRole:
                    index_of(index, Select2Group).set_name(value)
                    return True
            case Select2Option.__name__:
                if role == Qt.ItemDataRole.DisplayRole:
                    index_of(index, Select2Option).set_title(value)
                    return True
                elif role == Qt.ItemDataRole.UserRole:
                    index_of(index, Select2Option).set_data(value)
                    return True

        return False

    @method(InsertCycle)
    def insertRows(self, row, count, parent=QModelIndex()):
        match self.item_type(parent).__name__:
            case Select2Container.__name__:
                for i in range(count):
                    self.container.add_group(row + i, Select2Group(self.container, self.group_id_provider.provide()))

                return True
            case Select2Group.__name__:
                group = index_of(parent, Select2Group)

                for i in range(count):
                    group.add_option(row + i, Select2Option(group))

                return True

        return False

    @method(RemoveCycle)
    def removeRows(self, row, count, parent=QModelIndex()):
        match self.item_type(parent).__name__:
            case Select2Container.__name__:
                for i in range(count):
                    self.container.remove_group(row)

                return True
            case Select2Group.__name__:
                group = index_of(parent, Select2Group)

                for i in range(count):
                    group.remove_option(row)

                return True

        return False

    @property
    def container(self):
        return self._container

    @property
    def group_id_provider(self):
        return self._group_id_provider
