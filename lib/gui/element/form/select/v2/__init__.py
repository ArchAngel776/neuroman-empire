from PyQt5.QtWidgets import QApplication

from lib.gui.element.form import FormControl
from lib.gui.element.form.select.v2.base import QComboBox2
from lib.gui.event.select_box_selected import SelectBoxSelectedEvent


# Main

class Select2Box(QComboBox2, FormControl):
    def __init__(self, root):
        super().__init__(root)

    def config(self):
        super().config()
        self.currentIndexChanged.connect(self.select_event)
        self.currentIndexChanged.connect(self.select_input)

    def showEvent(self, event):
        super().showEvent(event)
        self.select_event()

    def react(self, value):
        index, data = value
        self.setCurrentIndex(index)

    def select_event(self):
        QApplication.sendEvent(self, SelectBoxSelectedEvent(self.currentText(), self.currentData()))

    def select_input(self):
        self.input((self.currentIndex(), self.currentData()))

    def Group(self, group_id, name):
        self.addGroup(group_id, name)
        return self

    def Option(self, group_id, title, data):
        self.addOption(group_id, title, data)
        return self

    def Active(self, index):
        self.setCurrentIndex(index)
        return self
