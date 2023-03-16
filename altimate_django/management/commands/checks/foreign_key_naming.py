from .base_field_check import BaseFieldCheck
from django.db import models


class ForeignKeyNaming(BaseFieldCheck):
    def perform_field_check(self):
        field = self.field_info.field
        if isinstance(field, models.ForeignKey):
            expected_name = f"{field.related_model.__name__.lower()}_id"
            if field.name != expected_name:
                return {
                    "severity": "Low",
                    "description": "Foreign key field name does not follow the naming convention.",
                    "explanation": f"The field '{field.name}' should be named '{expected_name}'.",
                }
        return None
