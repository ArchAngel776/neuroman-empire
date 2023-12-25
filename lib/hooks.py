from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QWidget


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
