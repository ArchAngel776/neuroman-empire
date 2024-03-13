from typing import Self, Any, Optional

from PyQt5.QtCore import QObject


# Main

class Foundation(QObject):
    def Parent(self, parent: QObject) -> Self: ...

    def Name(self, name: str) -> Self: ...

    def Property(self, name: str, value: Any) -> Self: ...

    def Class(self, class_name: Optional[str]) -> Self: ...
