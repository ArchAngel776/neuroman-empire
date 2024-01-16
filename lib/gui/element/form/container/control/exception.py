import math

from PyQt5.QtCore import QPoint, QRect, Qt, QRectF, QSize
from PyQt5.QtGui import QPen, QColor, QPainter, QPainterPath
from PyQt5.QtWidgets import QRubberBand

from lib.gui.element.font import Font
from lib.helpers.font_measurer import FontMeasurer


# Main

class ValidatorException(QRubberBand):
    def __init__(self):
        super().__init__(QRubberBand.Shape.Rectangle)
        self._message = ""
        self._font_measurer = FontMeasurer()
        self._left_side = True

    def prepare(self, form_control):
        self.setParent(form_control.root)

        form_position = form_control.mapTo(form_control.root, QPoint())
        text_size = self._font_measurer.size(self._message, self.text_font)

        position = QPoint(form_position)
        position.setY(position.y() + form_control.size().height())

        size = QSize(text_size)
        size.setWidth(size.width() + 2 * self.stroke + 2 * self.padding)
        size.setHeight(size.height() + 2 * self.stroke + 2 * self.padding + self.arrow_height)

        if form_position.x() + text_size.width() < form_control.root.width():
            self._left_side = True
        elif form_position.x() + form_control.size().width() - text_size.width() > 0:
            self._left_side = False
            position.setX(
                position.x() + form_control.size().width() - text_size.width() - 2 * self.stroke - 2 * self.padding
            )
        else:
            raise ValueError("Size of exception is too big to display it on the screen.")

        self.setGeometry(QRect(position, size))
        return self

    def setMessage(self, message):
        self._message = message
        return self

    def open(self):
        return self.show() if self.isHidden() else self.repaint()

    def close(self):
        return self.hide()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.RenderHint.HighQualityAntialiasing | QPainter.RenderHint.TextAntialiasing)

        path = self.from_left_side(QPainterPath()) if self._left_side else self.from_right_side(QPainterPath())

        painter.setPen(self.pen)
        painter.setBrush(self.background_color)

        painter.drawPath(path)

        painter.setPen(self.text_pen)
        painter.setFont(self.text_font)

        painter.drawText(
            QRect(
                self.stroke + self.padding, self.arrow_height + self.stroke + self.padding,
                self.size.width() - 2 * self.stroke - 2 * self.padding,
                self.size.height() - 2 * self.stroke - 2 * self.padding - self.arrow_height
            ),
            Qt.AlignCenter,
            self.message
        )

    def from_left_side(self, path):
        path.moveTo(QPoint(self.stroke, self.arrow_height + self.radius + self.stroke))
        path.arcTo(
            QRectF(self.stroke, self.arrow_height + self.stroke, self.radius * 2, self.radius * 2),
            180, -90
        )
        path.lineTo(self.radius * 2 + self.stroke, self.arrow_height + self.stroke)
        path.lineTo(self.arrow_side / 2 + self.radius * 2 + self.stroke, self.stroke)
        path.lineTo(self.arrow_side + self.radius * 2 + self.stroke, self.arrow_height + self.stroke)
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
            QRectF(self.stroke, self.size.height() - self.radius * 2 - self.stroke, self.radius * 2, self.radius * 2),
            270, -90
        )
        path.lineTo(self.stroke, self.arrow_height + self.radius + self.stroke)

        return path

    def from_right_side(self, path):
        path.moveTo(QPoint(self.size.width() - self.stroke, self.arrow_height + self.radius + self.stroke))
        path.arcTo(
            QRectF(
                self.size.width() - self.radius * 2 - self.stroke, self.arrow_height + self.stroke,
                self.radius * 2, self.radius * 2
            ),
            0, 90
        )
        path.lineTo(self.size.width() - self.radius * 2 - self.stroke, self.arrow_height + self.stroke)
        path.lineTo(self.size.width() - self.arrow_side / 2 - self.radius * 2 - self.stroke, self.stroke)
        path.lineTo(self.size.width() - self.arrow_side - self.radius * 2 - self.stroke, self.arrow_height + self.stroke)
        path.lineTo(self.radius + self.stroke, self.arrow_height + self.stroke)
        path.arcTo(
            QRectF(self.stroke, self.arrow_height + self.stroke, self.radius * 2, self.radius * 2),
            90, 90
        )
        path.lineTo(self.stroke, self.size.height() - self.radius - self.stroke)
        path.arcTo(
            QRectF(self.stroke, self.size.height() - self.radius * 2 - self.stroke, self.radius * 2, self.radius * 2),
            180, 90
        )
        path.lineTo(self.size.width() - self.stroke - self.radius, self.size.height() - self.stroke)
        path.arcTo(
            QRectF(
                self.size.width() - self.radius * 2 - self.stroke, self.size.height() - self.radius * 2 - self.stroke,
                self.radius * 2, self.radius * 2
            ),
            270, 90
        )
        path.lineTo(self.size.width() - self.stroke, self.arrow_height + self.radius + self.stroke)

        return path

    @property
    def message(self):
        return self._message

    @property
    def size(self):
        return self.geometry().size()

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
    def text_color(self):
        return QColor(255, 255, 255)

    @property
    def stroke_color(self):
        return QColor(192, 0, 0)

    @property
    def background_color(self):
        return QColor(0, 0, 0, 192)

    @property
    def pen(self):
        return QPen(self.stroke_color, self.stroke)

    @property
    def text_pen(self):
        return QPen(self.text_color)

    @property
    def text_font(self):
        return Font().Size(12)
