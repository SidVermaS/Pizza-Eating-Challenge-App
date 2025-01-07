from flask_restful import fields

# app/fields.py
from flask_restful import fields


class EnumField(fields.Raw):
    def __init__(self, enum_type, *args, **kwargs):
        self.enum_type = enum_type
        super().__init__(*args, **kwargs)

    def format(self, value):
        if isinstance(value, self.enum_type):
            return value.value
        raise ValueError(f"Invalid value for enum {self.enum_type.__name__}")
