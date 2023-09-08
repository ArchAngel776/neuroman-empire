import yaml


# Main

class YAML:
    XPATH_SPLITER = "."

    def __init__(self, path):
        self._path = path

    def load(self):
        with open(self.path, "rb") as y:
            return yaml.load(y.read(), yaml.CSafeLoader)

    def xpath(self, xpath):
        value = self.load()
        for key in xpath.split(YAML.XPATH_SPLITER):
            if isinstance(value, dict):
                value = value[key]
            elif isinstance(value, list):
                value = value[int(key)]
            else:
                raise ValueError("Not possible iteration")
        return value

    @property
    def path(self):
        return self._path
