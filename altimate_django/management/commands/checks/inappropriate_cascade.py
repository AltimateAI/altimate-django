from .base_field_check import BaseFieldCheck
from django.db import models


class InappropriateCascade(BaseFieldCheck):
    def perform_field_check(self):
        field = self.field_info.field
        if (
            isinstance(field, models.ForeignKey)
            and field.remote_field.on_delete == models.CASCADE
        ):
            return {
                "field_name": field.name,
                "severity": "Medium",
                "description": "Inappropriate use of CASCADE on ForeignKey",
                "explanation": "Using on_delete=models.CASCADE can lead to unexpected data loss when a related object is deleted. Review your use of CASCADE and consider using alternative options like SET_NULL or PROTECT if appropriate.",
            }

        return None
