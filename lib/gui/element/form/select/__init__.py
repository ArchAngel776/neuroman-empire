from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QComboBox, QCompleter, QTreeView, QListView

from lib.gui.element.form import FormControl
from lib.gui.element.form.select.item import SelectItem
from lib.gui.element.form.select.item.type import SelectItemType
from lib.gui.element.form.select.list import List
from lib.gui.element.form.select.model import SelectModel
from lib.gui.element.form.select.view import SelectView
from lib.gui.event.select_box_selected import SelectBoxSelectedEvent


# Main

class SelectBox(QComboBox, FormControl):
    def __init__(self, root):
        super().__init__(root)
        # self.setModel(SelectModel(self))
        # self.setView(List(self))
        # print(self.model())
        # print(self.view())

    def config(self):
        super().config()
        self.currentIndexChanged.connect(self.select_event)
        self.currentIndexChanged.connect(self.select_input)

    def showEvent(self, event):
        super().showEvent(event)
        self.select_event(self.currentIndex())

    def react(self, value):
        index, data = value
        self.setCurrentIndex(index)

    def select_event(self, index):
        QCoreApplication.sendEvent(self, SelectBoxSelectedEvent(self.itemText(index), self.itemData(index)))

    def select_input(self, index):
        self.input((index, self.itemData(index)))

    def Group(self, title: str):
        # self.addItem(title)
        '''
        if self.model().insertRow(self.model().rowCount()):
            index = self.model().index(self.model().rowCount() - 1, 0)
            self.model().setItemData(index, {
                Qt.ItemDataRole.DisplayRole: title
            })
        '''
        '''
        if self.model().insertRow(self.model().rowCount()):
            index = self.model().index(self.model().rowCount() - 1, 0)
            self.model().setItemData(index, {
                Qt.ItemDataRole.DisplayRole: title
            })
        '''
        return self

    def Option(self, group, title, data=None):
        self.addItem(title, data)
        '''
        for i in range(self.model().rowCount()):
            index = self.model().index(i, 0)
            if self.model().data(index, Qt.ItemDataRole.DisplayRole) == group:
                if self.model().insertRow(self.model().rowCount(index), index):
                    sub_index = self.model().index(self.model().rowCount(index) - 1, 0, index)
                    self.model().setItemData(sub_index, {
                        Qt.ItemDataRole.DisplayRole: title
                    })
        '''
        return self

    def Active(self, index):
        self.setCurrentIndex(index)
        '''
        for i in range(self.model().rowCount()):
            index = self.model().index(i, 0)
            for j in range(self.model().rowCount(index)):
                sub_index = self.model().index(j, 0, index)
                print(self.model().itemData(sub_index))
        '''
        return self

    def V2(self, enabled=True):
        if enabled:
            self.setEditable(True)
            self.completer().setCompletionMode(QCompleter.PopupCompletion)
        else:
            self.setEditable(False)
        return self
