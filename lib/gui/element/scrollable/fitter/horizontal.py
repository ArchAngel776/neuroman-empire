from lib.gui.element.scrollable.fitter import ScrollableFitter


# Main

class ScrollableHorizontalFitter(ScrollableFitter):
    def fitting(self, content, event):
        self.area.setFixedWidth(event.size().width() + self.additional_size(content))
        return True

    def is_scrollbar_visible(self, content):
        return content.height() > self.area.height()

    @property
    def scrollbar_size(self):
        return self.area.verticalScrollBar().width()
