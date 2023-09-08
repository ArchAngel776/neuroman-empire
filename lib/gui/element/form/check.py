from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QCheckBox

from lib.gui.element.form import FormControl
from lib.gui.event.check_box_changed import CheckBoxChangedEvent


# Main

class CheckBox(QCheckBox, FormControl):
    def __init__(self, root, checked):
        super().__init__(root)
        self.setChecked(checked)

    def config(self):
        super().config()
        self.stateChanged.connect(self.change_event)
        self.stateChanged.connect(self.change_input)

    def showEvent(self, event):
        super().showEvent(event)
        self.change_event()

    def change_event(self):
        QCoreApplication.sendEvent(self, CheckBoxChangedEvent(self.isChecked()))

    def change_input(self):
        self.input(self.isChecked())
