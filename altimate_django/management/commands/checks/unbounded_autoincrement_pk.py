from .base_field_check import BaseFieldCheck
from django.db import models


class UnboundedAutoIncrementPK(BaseFieldCheck):
    def perform_field_check(self):
        field = self.field_info.field
        if (
            isinstance(field, models.IntegerField)
            and field.primary_key
            and field.max_length is None
        ):
            return {
                "field": field.name,
                "severity": "Warning",
                "description": "Unbounded auto-incrementing primary key",
                "explanation": "Models with auto-incrementing primary keys should have a maximum value set to prevent potential issues with running out of primary key values.",
            }

        return None
