import math

from PyQt5.QtCore import QRect, Qt, QPoint, QRectF
from PyQt5.QtGui import QPainter, QColor, QPen, QPainterPath
from PyQt5.QtWidgets import QRubberBand


# Main

class ValidationException(QRubberBand):
    def __init__(self, field):
        super().__init__(QRubberBand.Rectangle, field.root)
        self._field = field
        self._text = ""

        self._pen = QPen()
        self._background_color = QColor(0, 0, 0, 192)

        self._text_pen = QPen()

    def config(self):
        self._pen.setColor(QColor(192, 0, 0))
        self._pen.setWidth(self.stroke)

        self._text_pen.setColor(QColor(255, 255, 255))

    def setup(self):
        self.setGeometry(QRect(self.position, self.size))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.RenderHint.HighQualityAntialiasing | QPainter.RenderHint.TextAntialiasing)

        path = QPainterPath(QPoint(self.stroke, self.arrow_height + self.radius + self.stroke))
        path.arcTo(
            QRectF(
                self.stroke, self.arrow_height + self.stroke,
                self.radius * 2, self.radius * 2
            ),
            180, -90
        )
        path.lineTo(self.arrow_side, self.arrow_height + self.stroke)
        path.lineTo(self.arrow_side * 1.5, self.stroke)
        path.lineTo(self.arrow_side * 2, self.arrow_height + self.stroke)
        path.lineTo(self.size.width() - self.radius - self.stroke, self.arrow_height + self.stroke)
        path.arcTo(
            QRectF(
                self.size.width() - self.radius * 2 - self.stroke, self.arrow_height + self.stroke,
                self.radius * 2, self.radius * 2
            ),
            90, -90
        )
        path.lineTo(self.size.width() - self.stroke, self.size.height() - self.radius - self.stroke)
        path.arcTo(
            QRectF(
                self.size.width() - self.radius * 2 - self.stroke, self.size.height() - self.radius * 2 - self.stroke,
                self.radius * 2, self.radius * 2
            ),
            0, -90
        )
        path.lineTo(self.stroke + self.radius, self.size.height() - self.stroke)
        path.arcTo(
            QRectF(
                self.stroke, self.size.height() - self.radius * 2 - self.stroke,
                self.radius * 2, self.radius * 2
            ),
            270, -90
        )
        path.lineTo(self.stroke, self.arrow_height + self.radius + self.stroke)

        painter.setPen(self._pen)
        painter.setBrush(self._background_color)

        painter.drawPath(path)

        painter.setPen(self._text_pen)

        painter.drawText(
            QRect(
                self.stroke + self.padding, self.arrow_height + self.stroke + self.padding,
                self.size.width() - 2 * self.stroke - 2 * self.padding,
                self.size.height() - 2 * self.stroke - 2 * self.padding - self.arrow_height
            ),
            Qt.AlignCenter | Qt.TextWordWrap,
            self.text
        )

    def set_text(self, text):
        self._text = text

    @property
    def position(self):
        position = self._field.position
        position.setY(position.y() + self._field.size.height())
        return position

    @property
    def size(self):
        size = self._field.size
        size.setHeight(size.height() * 2 + self.arrow_height)
        return size

    @property
    def arrow_side(self):
        return 16

    @property
    def arrow_height(self):
        return int(self.arrow_side * math.sqrt(3) / 2)

    @property
    def stroke(self):
        return 2

    @property
    def radius(self):
        return 4

    @property
    def padding(self):
        return 8

    @property
    def text(self):
        return self._text
