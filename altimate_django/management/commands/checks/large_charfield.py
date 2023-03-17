from .base_field_check import BaseFieldCheck
from django.db import models


class LargeCharField(BaseFieldCheck):
    def perform_field_check(self):
        field = self.field_info.field
        large_charfield_threshold = 255
        if (
            isinstance(field, models.CharField)
            and field.max_length
            and field.max_length > large_charfield_threshold
        ):
            return {
                "severity": "Warning",
                "description": f"Field {field.name} has a large max_length of {field.max_length}. Consider using TextField instead of CharField for storing long strings.",
                "explanation": "TextField is more efficient for storing and retrieving long text values. Changing a large CharField to TextField can improve performance and reduce the likelihood of reaching the maximum allowed length for a character field.",
            }
        return None
