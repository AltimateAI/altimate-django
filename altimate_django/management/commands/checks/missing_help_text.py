from .base_field_check import BaseFieldCheck
from django.db import models


class MissingHelpText(BaseFieldCheck):
    def perform_field_check(self):
        field = self.field_info.field
        if (
            not isinstance(field, models.ManyToManyField)
            and not field.auto_created
            and not field.help_text
        ):
            return {
                "severity": "Low",
                "description": f"Field {field.name} does not have help_text. Consider adding help_text to provide a description of the field's purpose.",
                "explanation": "Help text provides additional context and guidance for users interacting with the field, such as in the Django admin interface or other forms. Adding help_text can improve user experience and reduce confusion.",
            }
        return None
