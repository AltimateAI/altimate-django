from .base_field_check import BaseFieldCheck
from django.db import models
from django.db.models.fields import DateField, DateTimeField


class MissingDefault(BaseFieldCheck):
    def perform_field_check(self):
        field = self.field_info.field
        is_date_or_datetime = isinstance(field, (DateField, DateTimeField))

        if (
            not field.null
            and not field.has_default()
            and (not is_date_or_datetime or not (field.auto_now or field.auto_now_add))
        ):
            return {
                "severity": "Warning",
                "description": f"Field {field.name} should have a default value or be nullable",
                "explanation": "Having a default value or allowing null values for a field can prevent issues when creating new records, making it easier to handle cases where a value is not provided.",
            }
        return None
