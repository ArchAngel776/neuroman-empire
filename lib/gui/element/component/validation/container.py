# Main

class ValidationContainer:
    def __init__(self):
        self._validation_fields = []

    def register_field(self, validation_field):
        self._validation_fields.append(validation_field)

    def validate(self):
        valid = True
        for validation_field in self._validation_fields:
            if not validation_field.validate_container():
                valid = False
        return valid

    @property
    def validation_fields(self):
        return self._validation_fields
