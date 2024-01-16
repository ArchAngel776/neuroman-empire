from PyQt5.QtGui import QFontMetrics


# Main

class FontMeasurer:
    def size(self, text, font):
        return self.metrics(font).boundingRect(text).size()

    @staticmethod
    def metrics(font):
        return QFontMetrics(font)
