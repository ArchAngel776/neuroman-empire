from lib import REM_SIZE
from lib.decorators import method
from lib.decorators.decorator import Decorator


# Decorators

class MarginValidation(Decorator):
    def method(self, size):
        return int(super().method(size))


class ExistsWatcher(Decorator):
    def method(self, target, key, updater):
        if target.watcher_exists(key):
            super().method(target, key, updater)


# Foundations

class LS:
    @staticmethod
    @method(MarginValidation)
    def rem(size: float):
        return REM_SIZE * size


# Base

class Watcher:
    def __init__(self):
        self._watched = {}

    def watcher_exists(self, key):
        return key in self._watched

    def watch(self, key, element):
        self._watched[key] = element
        return element

    def get(self, key):
        return self._watched[key]

    @method(ExistsWatcher)
    def update(self, key, updater):
        updater(self._watched[key])
