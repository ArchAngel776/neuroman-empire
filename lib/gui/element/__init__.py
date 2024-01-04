from PyQt5.QtWidgets import QWidget

from lib.events.emitter import EventEmitter
from lib.hooks import app


# Main

class Element(QWidget, EventEmitter):
    def __init__(self, root):
        super().__init__(parent=root)

    def config(self):
        pass

    def event(self, event):
        return super().event(event) if self.emit(event.type(), event) else False

    def Name(self, name):
        self.setObjectName(name)
        return self

    def Property(self, name, value):
        self.setProperty(name, value)
        return self

    def Class(self, class_name):
        self.setProperty("class", class_name)
        return self

    def Sizing(self, horizontal, vertical):
        self.setSizePolicy(horizontal, vertical)
        return self

    def Width(self, width):
        self.setFixedWidth(width)
        return self

    def MinWidth(self, width):
        self.setMinimumWidth(width)
        return self

    def MaxWidth(self, width):
        self.setMaximumWidth(width)
        return self

    def Height(self, height):
        self.setFixedHeight(height)
        return self

    def MinHeight(self, height):
        self.setMinimumHeight(height)
        return self

    def MaxHeight(self, height):
        self.setMaximumHeight(height)
        return self

    def Hidden(self, hidden=True):
        self.setHidden(hidden)
        return self

    def Font(self, font):
        self.setFont(font)
        return self

    def Cursor(self, cursor):
        self.setCursor(cursor)
        return self

    def ToolTip(self, tip):
        self.setToolTip(tip)
        return self

    def Margin(self, horizontal, vertical):
        self.setContentsMargins(horizontal, vertical, horizontal, vertical)
        return self

    def On(self, event, callback, with_target=True, with_event=True):
        self.add_event_listener(event, callback, with_target, with_event)
        return self

    def update_style(self):
        app().style().polish(self)

    @property
    def root(self):
        return self.parent()
