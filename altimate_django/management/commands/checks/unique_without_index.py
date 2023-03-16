from .base_field_check import BaseFieldCheck
from django.db import models


class UniqueWithoutIndex(BaseFieldCheck):
    def perform_field_check(self):
        field = self.field_info.field
        if (
            not isinstance(field, models.ManyToManyField)
            and hasattr(field, "unique")
            and field.unique
            and not field.db_index
        ):
            return {
                "severity": "Warning",
                "description": f"Field {field.name} has unique=True but no index. Consider adding an index to improve query performance.",
                "explanation": "An index can speed up lookups for unique values, making queries more efficient. Adding an index to a unique field can improve the overall performance of your database.",
            }
        return None
