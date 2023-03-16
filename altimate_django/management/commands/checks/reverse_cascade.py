from .base_field_check import BaseFieldCheck
from django.db import models


# This check will fail if a ForeignKey or OneToOneField is set to CASCADE
# delete and does not allow null values. This is a best practice, as it
# prevents unintended data loss when related records are deleted.
class ReverseCascade(BaseFieldCheck):
    def perform_field_check(self):
        field = self.field_info.field
        # If the field is a ForeignKey or OneToOneField, and the on_delete
        # rule is CASCADE, and the field does not allow null values, raise
        # a warning.
        if isinstance(field, (models.ForeignKey, models.OneToOneField)):
            if (
                field.remote_field.on_delete == models.CASCADE
                and not field.null
            ):
                return {
                    "severity": "Warning",
                    "description": f"Field {field.name} should allow null values or use a different delete rule",
                    "explanation": "When using CASCADE as the delete rule for a ForeignKey or OneToOneField, it is a best practice to allow null values. This prevents unintended data loss when related records are deleted.",
                }
        return None
