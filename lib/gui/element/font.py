from PyQt5.QtGui import QFont


# Main

class Font(QFont):
    def Size(self, size):
        self.setPixelSize(size)
        return self

    def Bold(self, bold=True):
        self.setBold(bold)
        return self

    def Italic(self, italic=True):
        self.setItalic(italic)
        return self

    def Underline(self, underline=True):
        self.setUnderline(underline)
        return self
