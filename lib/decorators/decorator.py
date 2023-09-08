# Main

class Decorator:
    def __init__(self, original):
        self._original = original

    def config(self, *args, **kwargs):
        return self

    def method(self, *args, **kwargs):
        return self._original(*args, **kwargs)
