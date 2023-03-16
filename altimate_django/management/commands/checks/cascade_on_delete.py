from .base_field_check import BaseFieldCheck
from django.db import models


class CascadeOnDelete(BaseFieldCheck):
    """
    This class checks if the `on_delete` attribute of ForeignKey and OneToOneField fields
    is set to CASCADE to maintain database integrity.

    Inherits from the `BaseFieldCheck` class.
    """

    def perform_field_check(self):
        """
        Checks if the `on_delete` attribute of the field is set to CASCADE for ForeignKey and
        OneToOneField fields.

        Returns:
            dict: A dictionary containing information about the field if the check fails, otherwise None.
        """
        field = self.field_info.field
        if (
            isinstance(field, (models.ForeignKey, models.OneToOneField))
            and field.remote_field.on_delete != models.CASCADE
        ):
            return {
                "field": field.name,
                "severity": "Medium",
                "description": "Missing CASCADE on ForeignKey or OneToOneField",
                "explanation": "ForeignKey and OneToOneField fields should use on_delete=models.CASCADE to ensure database integrity.",
            }
        return None
