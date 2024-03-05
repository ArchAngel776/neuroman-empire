from PyQt5.QtCore import QObject


# Main

class Foundation(QObject):
    def Parent(self, parent):
        self.setParent(parent)
        return self

    def Name(self, name):
        self.setObjectName(name)
        return self

    def Property(self, name, value):
        self.setProperty(name, value)
        return self

    def Class(self, class_name):
        self.setProperty("class", class_name)
        return self
