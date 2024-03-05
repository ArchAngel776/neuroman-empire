from typing import Optional

from PyQt5.QtWidgets import QProxyStyle, QStyle, QWidget, QStyleOption, QStyleHintReturn

from lib.foundations import Foundation


# Main

class Select2ViewStyle(QProxyStyle, Foundation):
    def styleHint(
            self,
            hint: QStyle.StyleHint,
            option: Optional[QStyleOption] = ...,
            widget: Optional[QWidget] = ...,
            returnData: Optional[QStyleHintReturn] = ...
    ) -> QStyle.StyleHint: ...