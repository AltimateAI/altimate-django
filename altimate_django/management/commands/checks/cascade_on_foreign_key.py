from .base_field_check import BaseFieldCheck
from django.db import models


class CascadeOnForeignKey(BaseFieldCheck):
    """
    This class checks if the `on_delete` attribute of ForeignKey fields
    is set to CASCADE and raises a warning about potential data loss.

    Inherits from the `BaseFieldCheck` class.
    """

    def perform_field_check(self):
        """
        Checks if the `on_delete` attribute of the field is set to CASCADE for ForeignKey fields
        and raises a warning about potential data loss.

        Returns:
            dict: A dictionary containing information about the field if the check fails, otherwise None.
        """
        field = self.field_info.field
        if (
            isinstance(field, models.ForeignKey)
            and field.remote_field.on_delete == models.CASCADE
        ):
            return {
                "field": field.name,
                "severity": "High",
                "description": "Inappropriate use of CASCADE on ForeignKey",
                "explanation": "Using on_delete=models.CASCADE can lead to unexpected data loss when a related object is deleted. Review your use of CASCADE and consider using alternative options like SET_NULL or PROTECT if appropriate.",
            }
        return None
