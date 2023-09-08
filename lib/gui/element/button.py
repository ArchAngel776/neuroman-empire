from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QPushButton

from lib.gui.element import Element
from lib.gui.event.button_click import ButtonClickEvent


# Main

class Button(QPushButton, Element):
    def __init__(self, root, text):
        super().__init__(root)
        self.setText(text)

    def config(self):
        super().config()
        self.clicked.connect(self.click_event)

    def click_event(self):
        QCoreApplication.sendEvent(self, ButtonClickEvent())
