# Main

class I18NMessage(str):
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message
