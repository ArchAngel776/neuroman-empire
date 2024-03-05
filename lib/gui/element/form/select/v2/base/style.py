from PyQt5.QtWidgets import QProxyStyle, QStyle, QComboBox

from lib.foundations import Foundation


# Main

class Select2BoxStyle(QProxyStyle, Foundation):
    def subControlRect(self, cc, opt, sc, widget):
        rect = super().subControlRect(cc, opt, sc, widget)

        if cc == QStyle.ComplexControl.CC_ComboBox and sc == QStyle.SubControl.SC_ComboBoxListBoxPopup:
            assert isinstance(widget, QComboBox)
            rect.setTop(rect.top() + widget.view().visualRect(widget.view().currentIndex()).top())

        return rect
