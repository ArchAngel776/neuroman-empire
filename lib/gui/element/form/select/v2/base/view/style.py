from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QProxyStyle

from lib.foundations import Foundation


# Main

class Select2ViewStyle(QProxyStyle, Foundation):
    def styleHint(self, hint, option=None, widget=None, returnData=None):
        if hint == QProxyStyle.StyleHint.SH_ListViewExpand_SelectMouseType:
            return QEvent.MouseButtonRelease

        return super().styleHint(hint, option, widget, returnData)
