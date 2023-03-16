from .base_field_check import BaseFieldCheck
from django.db import models


class ExcessiveBlanks(BaseFieldCheck):
    def perform_field_check(self):
        field = self.field_info.field
        # Check if the field is a ManyToManyField
        if (
            not isinstance(field, models.ManyToManyField)
            and not isinstance(field, models.ManyToManyRel)
            and not isinstance(field, models.ManyToOneRel)
        ):
            if field.blank:
                return {
                    "field_name": field.name,
                    "severity": "Info",
                    "description": f"Excessive use of blank=True",
                    "explanation": "Using blank=True excessively may cause issues with data consistency and validation. Review your use of blank=True in this field and consider removing it if it's not necessary.",
                }
        return None
