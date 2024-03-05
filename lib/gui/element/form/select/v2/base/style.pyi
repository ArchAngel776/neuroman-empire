from typing import Optional

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QProxyStyle, QStyle, QWidget, QStyleOptionComplex

from lib.foundations import Foundation


# Main

class Select2BoxStyle(QProxyStyle, Foundation):
    def subControlRect(
            self,
            cc: QStyle.ComplexControl,
            opt: Optional[QStyleOptionComplex],
            sc: QStyle.SubControl,
            widget: Optional[QWidget]
    ) -> QRect: ...
