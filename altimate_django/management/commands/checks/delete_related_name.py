from .base_field_check import BaseFieldCheck
from django.db import models


class RelatedName(BaseFieldCheck):
    def perform_field_check(self):
        field = self.field_info.field
        if isinstance(field, (models.ForeignKey, models.OneToOneField)):
            print(field.related_query_name())
            if not field.related_query_name():
                return {
                    "severity": "Warning",
                    "description": f"Field {field.name} should have a related_name",
                    "explanation": "Adding a related_name to ForeignKey and OneToOneField relationships can improve code readability and make it easier to access related records in reverse relationships.",
                }
        return None
