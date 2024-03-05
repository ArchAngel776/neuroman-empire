from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QComboBox

from lib.gui.element.form import FormControl
from lib.gui.event.select_box_selected import SelectBoxSelectedEvent


# Main

class SelectBox(QComboBox, FormControl):
    def __init__(self, root):
        super().__init__(root)

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

    def Option(self, title, data):
        self.addItem(title, data)
        return self

    def Active(self, index):
        self.setCurrentIndex(index)
        return self
