from PyQt5.QtCore import pyqtSignal, QModelIndex
from PyQt5.QtWidgets import QTreeView, QFrame

from lib.gui.element.form.select.v2.base.view.style import Select2ViewStyle


# Main

class Select2View(QTreeView):
    def __init__(self, parent):
        super().__init__(parent)

        self.setStyle(Select2ViewStyle().Parent(self))

        self.setUniformRowHeights(True)
        self.setExpandsOnDoubleClick(False)
        self.setHeaderHidden(True)

        self.clicked.connect(self.toggleGroup)
        self.expanded.connect(self.closeTheRest)

        self.expanded.connect(self.adjustContentFrame)
        self.collapsed.connect(self.adjustContentFrame)

    def currentChanged(self, current, previous):
        super().currentChanged(current, previous)
        self.expand(current.parent())

    # Slots

    def toggleGroup(self, index):
        self.collapse(index) if self.isExpanded(index) else self.expand(index)

    def closeTheRest(self, index):
        for row in range(self.model().rowCount(index.parent())):
            if row == index.row():
                continue

            group = self.model().index(row, 0, index.parent())
            self.collapse(group)

    def adjustContentFrame(self):
        frame = self.parent()
        assert isinstance(frame, QFrame)

        height = 0

        for row in range(self.model().rowCount()):
            for column in range(self.model().columnCount()):
                group = self.model().index(row, column)
                assert group.isValid()

                height += self.visualRect(group).height()

                if not self.isExpanded(group):
                    continue

                for sub_row in range(self.model().rowCount(group)):
                    for sub_column in range(self.model().columnCount(group)):
                        option = self.model().index(sub_row, sub_column, group)
                        assert option.isValid()

                        height += self.visualRect(option).height()

        height += frame.contentsMargins().top() + frame.contentsMargins().bottom()
        height += self.contentsMargins().top() + self.contentsMargins().bottom()

        geometry = frame.geometry()
        geometry.setHeight(height)

        frame.setGeometry(geometry)
