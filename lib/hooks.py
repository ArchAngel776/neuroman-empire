from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QWidget, QApplication


# Modules

def entities(target):
    target = list(target)
    return [(i, target[i]) for i in range(len(target))]


def pairs(target):
    target = list(target)
    return [(target[i], target[i + 1]) for i in range(len(target) - 1)] if len(target) >= 2 else []


def layout_widget(layout):
    widget = QWidget()
    widget.setLayout(layout)
    return widget


def palette_color(role, color):
    palette = QPalette()
    palette.setColor(role, color)
    return palette


def foreach(target, callback):
    for index, item in entities(target):
        callback(item, index)


def mapping(target, callback):
    return [callback(item, index) for index, item in entities(target)]


def merge(**sources):
    result = []
    for name in sources:
        for index, item in entities(sources[name]):
            if not index < len(result):
                result.append({})
            result[index][name] = item
    return result


def app():
    app = QApplication.instance()
    if isinstance(app, QApplication):
        return app
    raise TypeError("Application core hasn't been initialized or isn't proper core component.")


def bytes_to_string(target):
    return str(target, "utf-8")


def index_of(index, item_type):
    pointer = index.internalPointer()
    if isinstance(pointer, item_type):
        return pointer
    raise TypeError("Cannot fetch internal pointer of index into specified item type.")


def is_index(index, *item_type):
    return isinstance(index.internalPointer(), item_type)


def length(iterable):
    return sum(1 for _ in iterable)
