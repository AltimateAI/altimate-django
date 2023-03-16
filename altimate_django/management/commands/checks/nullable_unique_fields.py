from .base_field_check import BaseFieldCheck
from django.db import models


class NullableUniqueFields(BaseFieldCheck):
    def perform_field_check(self):
        field = self.field_info.field
        if isinstance(field, models.Field) and field.unique and field.null:
            return {
                "field_name": field.name,
                "severity": "Medium",
                "description": "Nullable unique field",
                "explanation": "Nullable unique fields can cause unexpected issues when multiple records have null values. Consider using a non-nullable unique field with a default value instead.",
            }
        return None
