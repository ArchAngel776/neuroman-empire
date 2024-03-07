from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QComboBox

from lib.hooks import length, index_of, entities
from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.foundations.data_provider.string_list_provider import StringListProvider
from lib.foundations.data_provider.model_index_provider import ModelIndexProvider
from lib.helpers.index_helper import IndexHelper
from lib.gui.element.form.select.v2.base.style import Select2BoxStyle
from lib.gui.element.form.select.v2.data.group import Select2Group
from lib.gui.element.form.select.v2.base.model import Select2Model
from lib.gui.element.form.select.v2.base.view import Select2View


# Decorators

class PreventRoot(Decorator):
    def method(self, target, index):
        root = target.rootModelIndex()
        super().method(target, index)
        target.setRootModelIndex(root)


class EditableIndexChanged(Decorator):
    def method(self, target, text):
        if target.isEditable():
            target.setEditText(text)
        else:
            super().method(target, text)


class ClearRootProvider(Decorator):
    def method(self, target, index):
        target.root_index_provider.clear()
        super().method(target)


# Main

class QComboBox2(QComboBox):
    HIERARCHY_LEVEL = 2

    HITS = 1

    class Position(int):
        NONE = -1
        START = 0

    def __init__(self, parent=None):
        super().__init__(parent)

        self._index_helper = IndexHelper()
        self._group_id_provider = StringListProvider()
        self._root_index_provider = ModelIndexProvider()

        self.setModel(Select2Model(self, self.group_id_provider))
        self.setView(Select2View(self))

        self.setStyle(Select2BoxStyle().Parent(self))

        self.currentIndexChanged.connect(self.storeRoot)

        self.view().selectionModel().currentChanged.connect(self.view().setCurrentIndex)

    def addItem(self, text, userData=None):
        raise NotImplementedError(
            "Add Item method is not implemented in ComboBox2. Please use Add Group or Add Option instead."
        )

    def addItems(self, texts):
        raise NotImplementedError(
            "Add Items method is not implemented in ComboBox2. Please use Add Groups or Add Options instead."
        )

    def findData(
            self,
            data,
            role=Qt.ItemDataRole.UserRole,
            flags=Qt.MatchFlag.MatchExactly | Qt.MatchFlag.MatchCaseSensitive
    ):
        raise NotImplementedError(
            "Find Data method is not implemented in ComboBox2. Please use Find Option Data instead."
        )

    def findText(self, text, flags=Qt.MatchFlag.MatchExactly | Qt.MatchFlag.MatchCaseSensitive):
        raise NotImplementedError(
            "Find Text method is not implemented in ComboBox2. Please use Find Group Name or Find Option Title instead."
        )

    def insertItem(self, index, text, userData=None):
        raise NotImplementedError(
            "Insert Item method is not implemented in ComboBox2. Please use Insert Group or Insert Option instead."
        )

    def insertItems(self, index, texts):
        raise NotImplementedError(
            "Insert Items method is not implemented in ComboBox2. Please use Insert Groups or Insert Options instead."
        )

    def itemData(self, index, role=Qt.ItemDataRole.UserRole):
        raise NotImplementedError(
            "Item Data method is not implemented in ComboBox2. Please use Option Data instead."
        )

    def itemIcon(self, index):
        raise NotImplementedError(
            "Item Icon method is not implemented in ComboBox2."
        )

    def itemText(self, index):
        raise NotImplementedError(
            "Item Text method is not implemented in ComboBox2. Please use Group Text or Option Text instead."
        )

    def setItemData(self, index, value, role=Qt.ItemDataRole.UserRole):
        raise NotImplementedError(
            "Set Item Data method is not implemented in ComboBox2. Please use Set Option Data instead."
        )

    def setItemIcon(self, index, icon):
        raise NotImplementedError(
            "Set Item Icon method is not implemented in ComboBox2."
        )

    def setItemText(self, index, text):
        raise NotImplementedError(
            "Set Item Text method is not implemented in ComboBox2. "
            "Please use Set Group Text or Set Option Text instead."
        )

    def addGroup(self, group_id, name=None):
        self.insertGroup(self.model().rowCount(), group_id, name)

    def addGroups(self, group_ids):
        self.insertGroups(self.model().rowCount(), group_ids)

    def addOption(self, group_id, title, data=None):
        parent = self.model().index(self.findGroupId(group_id), self.modelColumn())

        if parent.isValid():
            self.insertOption(group_id, self.model().rowCount(parent), title, data)

    def addOptions(self, group_id, titles):
        parent = self.model().index(self.findGroupId(group_id), self.modelColumn())

        if parent.isValid():
            self.insertOptions(group_id, self.model().rowCount(parent), titles)

    def currentIndex(self):
        index = self.model().index(super().currentIndex(), self.modelColumn(), self.root_index_provider.provide())
        return self.index_helper.index_to_position(self.model(), index, QComboBox2.HIERARCHY_LEVEL)

    def findGroupId(self, group_id):
        for row in range(self.model().rowCount()):
            if self.groupId(row) == group_id:
                return row

        return QComboBox2.Position.NONE

    def findGroupName(self, name, flags=Qt.MatchFlag.MatchExactly | Qt.MatchFlag.MatchCaseSensitive):
        start = self.model().index(QComboBox2.START_ROW, self.modelColumn())
        indexes = self.model().match(start, Qt.ItemDataRole.DisplayRole, name, QComboBox2.HITS, flags)

        if len(indexes) > 0:
            return indexes[0].row()

        return QComboBox2.Position.NONE

    def findOptionTitle(self, group_id, title, flags=Qt.MatchFlag.MatchExactly | Qt.MatchFlag.MatchCaseSensitive):
        parent = self.model().index(self.findGroupId(group_id), self.modelColumn())

        if not parent.isValid():
            return

        start = self.model().index(QComboBox2.START_ROW, self.modelColumn(), parent)
        indexes = self.model().match(start, Qt.ItemDataRole.DisplayRole, title, QComboBox2.HITS, flags)

        if len(indexes) > 0:
            return indexes[0].row()

        return QComboBox2.Position.NONE

    def findOptionData(self, group_id, data, flags=Qt.MatchFlag.MatchExactly | Qt.MatchFlag.MatchCaseSensitive):
        parent = self.model().index(self.findGroupId(group_id), self.modelColumn())

        if not parent.isValid():
            return

        start = self.model().index(QComboBox2.START_ROW, self.modelColumn(), parent)
        indexes = self.model().match(start, Qt.ItemDataRole.UserRole, data, QComboBox2.HITS, flags)

        if len(indexes) > 0:
            return indexes[0].row()

        return QComboBox2.Position.NONE

    def groupId(self, index):
        group = self.model().index(index, self.modelColumn())
        assert group.isValid(), IndexError(f"Cannot find specified index position: {index} in the model.")

        return index_of(group, Select2Group).group_id

    def groupName(self, index):
        group = self.model().index(index, self.modelColumn())
        assert group.isValid(), IndexError(f"Cannot find specified index position: {index} in the model.")

        return self.model().data(group, Qt.ItemDataRole.DisplayRole)

    def insertGroup(self, index, group_id, name=None):
        self.group_id_provider.add(group_id)

        if not self.model().insertRow(index):
            self.group_id_provider.clear()
            return

        group = self.model().index(index, self.modelColumn())
        assert group.isValid()

        self.model().setData(group, name)

    def insertGroups(self, index, group_ids):
        self.group_id_provider.add(*group_ids)

        if not self.model().insertRows(index, length(group_ids)):
            self.group_id_provider.clear()

    def insertOption(self, group_id, index, title, data=None):
        group = self.model().index(self.findGroupId(group_id), self.modelColumn())

        if not (group.isValid() and self.model().insertRow(index, group)):
            return

        option = self.model().index(index, self.modelColumn(), group)

        self.model().setData(option, title)
        self.model().setData(option, data, Qt.ItemDataRole.UserRole)

    def insertOptions(self, group_id, index, titles):
        group = self.model().index(self.findGroupId(group_id), self.modelColumn())

        if not (group.isValid() and self.model().insertRows(index, length(titles), group)):
            return

        for i, title in entities(titles):
            option = self.model().index(index + i, self.modelColumn(), group)

            self.model().setData(option, title)

    def optionData(self, group_id, index):
        parent = self.model().index(self.findGroupId(group_id), self.modelColumn())
        assert parent.isValid(), IndexError(f"Cannot find specified group with ID: \"{group_id}\" in the model.")

        option = self.model().index(index, self.modelColumn(), parent)
        assert option.isValid(), IndexError(f"Cannot find specified index position: {index} "
                                            f"in the group \"{group_id}\" in the model.")

        return self.model().data(option, Qt.ItemDataRole.UserRole)

    def optionTitle(self, group_id, index):
        group = self.model().index(self.findGroupId(group_id), self.modelColumn())
        assert group.isValid(), IndexError(f"Cannot find specified group with ID: \"{group_id}\" in the model.")

        option = self.model().index(index, self.modelColumn(), group)
        assert option.isValid(), IndexError(f"Cannot find specified index position: {index} "
                                            f"in the group \"{group_id}\" in the model.")

        return self.model().data(option, Qt.ItemDataRole.DisplayRole)

    @method(PreventRoot)
    def setCurrentIndex(self, index):
        item = self.index_helper.position_to_index(self.model(), index, QComboBox2.HIERARCHY_LEVEL)
        assert item.isValid() and item.parent().isValid()

        self.setRootModelIndex(item.parent())
        super().setCurrentIndex(item.row())

    @method(EditableIndexChanged)
    def setCurrentText(self, text):
        accumulate = 0

        for row in range(self.model().rowCount()):
            group = self.model().index(row, self.modelColumn())

            group_id = self.groupId(group)
            position = self.findOptionTitle(group_id, text)

            if position == QComboBox2.Position.NONE:
                accumulate += self.model().rowCount(group)
                continue

            return self.setCurrentIndex(accumulate + position)

    def setGroupName(self, index, name):
        group = self.model().index(index, self.modelColumn())

        if not group.isValid():
            return

        self.model().setData(group, name, Qt.ItemDataRole.DisplayRole)

    def setOptionData(self, group_id, index, userData=None):
        group = self.model().index(self.findGroupId(group_id), self.modelColumn())

        if not group.isValid():
            return

        option = self.model().index(index, self.modelColumn(), group)

        if not option.isValid():
            return

        self.model().setData(option, userData, Qt.ItemDataRole.UserRole)

    def setOptionTitle(self, group_id, index, title):
        group = self.model().index(self.findGroupId(group_id), self.modelColumn())

        if not group.isValid():
            return

        option = self.model().index(index, self.modelColumn(), group)

        if not option.isValid():
            return

        self.model().setData(option, title, Qt.ItemDataRole.DisplayRole)

    # Slots

    @method(ClearRootProvider)
    def storeRoot(self):
        if self.view().currentIndex().isValid():
            root = self.view().currentIndex().parent()
        else:
            root = self.rootModelIndex()

        self.root_index_provider.add(root)

    @property
    def index_helper(self):
        return self._index_helper

    @property
    def group_id_provider(self):
        return self._group_id_provider

    @property
    def root_index_provider(self):
        return self._root_index_provider
