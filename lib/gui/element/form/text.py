from PyQt5.QtWidgets import QLineEdit, QApplication

from lib.gui.element.form import FormControl
from lib.gui.event.text_box_input_event import TextBoxInputEvent


# Main

class TextInput(QLineEdit, FormControl):
    def __init__(self, root, value):
        super().__init__(root)
        self.setText(value)

    def config(self):
        super().config()
        self.textChanged.connect(self.input)
        self.textChanged.connect(self.input_event)

    def react(self, value):
        self.setText(value)

    def Length(self, length):
        self.setMaxLength(length)
        return self

    def input_event(self, text):
        QApplication.sendEvent(self, TextBoxInputEvent(text))
