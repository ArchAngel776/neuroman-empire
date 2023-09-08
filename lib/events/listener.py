# Main

class EventListener:
    def __init__(self, callback, with_target, with_event):
        self._callback = callback
        self._with_target = with_target
        self._with_event = with_event

    @property
    def callback(self):
        return self._callback

    @property
    def with_target(self):
        return self._with_target

    @property
    def with_event(self):
        return self._with_event
