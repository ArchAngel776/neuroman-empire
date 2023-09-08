from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QComboBox

from lib.gui.element.form import FormControl
from lib.gui.event.select_box_selected import SelectBoxSelectedEvent


# Main

class SelectBox(QComboBox, FormControl):
    def config(self):
        super().config()
        self.currentIndexChanged.connect(self.select_event)
        self.currentIndexChanged.connect(self.select_input)

    def showEvent(self, event):
        super().showEvent(event)
        self.select_event(self.currentIndex())

    def select_event(self, index):
        QCoreApplication.sendEvent(self, SelectBoxSelectedEvent(self.itemText(index), self.itemData(index)))

    def select_input(self, index):
        self.input((index, self.itemData(index)))

    def Option(self, title, data=None):
        self.addItem(title, data)
        return self

    def Active(self, index):
        self.setCurrentIndex(index)
        return self
