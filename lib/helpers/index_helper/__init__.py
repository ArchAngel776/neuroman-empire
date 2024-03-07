from PyQt5.QtCore import QModelIndex, Qt

from lib.helpers.index_helper.counter import Counter


# Main

class IndexHelper:
    def index_to_position(self, model, index, level):
        counter = Counter()
        if self.recursive_index_to_position(model, index, level, counter.setup(QModelIndex())):
            return counter.position
        raise -1

    def position_to_index(self, model, position, level):
        counter = Counter()
        if self.recursive_position_to_index(model, position, level, counter) and counter.index.isValid():
            return counter.index
        return QModelIndex()

    def recursive_index_to_position(self, model, index, level, counter, current_level=0):
        if current_level == level:
            if counter.index == index:
                return True
            else:
                counter.increment_position()
                return False

        for row in range(model.rowCount(counter.index)):
            for column in range(model.columnCount(counter.index)):
                item = model.index(row, column, counter.index)
                assert item.isValid()

                current = counter.index

                if self.recursive_index_to_position(model, index, level, counter.setup(item), current_level + 1):
                    return True

                counter.setup(current)

        return False

    def recursive_position_to_index(self, model, position, level, counter, current_level=0, parent=QModelIndex()):
        if current_level == level:
            if counter.position == position:
                counter.setup(parent)
                return True
            else:
                counter.increment_position()
                return False

        for row in range(model.rowCount(parent)):
            for column in range(model.columnCount(parent)):
                item = model.index(row, column, parent)
                assert item.isValid()

                if self.recursive_position_to_index(model, position, level, counter, current_level + 1, item):
                    return True

        return False
