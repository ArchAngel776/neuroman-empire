from lib.hooks import entities
from lib.gui.element.component import Component
from lib.gui.layout.factory import LayoutFactory


# Main

class List(Component):
    def __init__(self, root, source_getter, orientation):
        super().__init__(root, orientation)
        self._source_getter = source_getter
        self._callback_builder = None

    def config(self):
        super().config()
        self.update_view()

    def Render(self, callback_builder):
        self._callback_builder = callback_builder
        return self

    def render_view(self, root):
        return (
            LayoutFactory(self._orientation).create()
            .append(
                *map(self.render_item, entities(self._source_getter()))
            )
        )

    def render_item(self, data):
        index, item = data
        return self.callback_builder(item, index)

    @property
    def callback_builder(self):
        if not self._callback_builder:
            raise AttributeError("Callback builder hasn't been provided yet.")
        return self._callback_builder
