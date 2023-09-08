from PyQt5.QtWidgets import QLineEdit

from lib.gui.element.form import FormControl


# Main

class TextInput(QLineEdit, FormControl):
    def __init__(self, root, value):
        super().__init__(root)
        self.setText(value)

    def config(self):
        super().config()
        self.textChanged.connect(self.input)

    def Length(self, length):
        self.setMaxLength(length)
        return self
