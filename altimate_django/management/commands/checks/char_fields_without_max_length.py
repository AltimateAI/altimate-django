from .base_field_check import BaseFieldCheck
from django.db import models


class CharFieldsWithoutMaxLength(BaseFieldCheck):
    def perform_field_check(self):
        field = self.field_info.field
        if isinstance(field, models.CharField) and not field.max_length:
            return {
                "field_name": field.name,
                "severity": "High",
                "description": "CharField without max_length",
                "explanation": "CharField should have max_length set to ensure data consistency and prevent potential issues with data storage.",
            }
        return None
