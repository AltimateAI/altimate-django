from .base_field_check import BaseFieldCheck
from django.db import models


class MissingRelatedNames(BaseFieldCheck):
    def perform_field_check(self):
        field = self.field_info.field
        if (
            isinstance(field, (models.ForeignKey, models.OneToOneField))
            and not field.related_query_name()
        ):
            return {
                "field_name": field.name,
                "severity": "Low",
                "description": "Missing related_name attribute",
                "explanation": "ForeignKey and OneToOneField fields should have a related_name attribute set to make reverse lookups more intuitive and prevent naming conflicts with reverse accessor names.",
            }
        return None
