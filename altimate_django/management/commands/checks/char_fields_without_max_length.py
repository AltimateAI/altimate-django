from .base_field_check import BaseFieldCheck
from django.db import models


class CharFieldsWithoutMaxLength(BaseFieldCheck):
    """
    This class checks if the `max_length` attribute of CharField fields
    is set to prevent potential issues with data storage and ensure data consistency.

    Inherits from the `BaseFieldCheck` class.
    """

    def perform_field_check(self):
        """
        Checks if the `max_length` attribute of the field is set for CharField fields.

        Returns:
            dict: A dictionary containing information about the field if the check fails, otherwise None.
        """
        field = self.field_info.field
        if isinstance(field, models.CharField) and not field.max_length:
            return {
                "field_name": field.name,
                "severity": "High",
                "description": "CharField without max_length",
                "explanation": "CharField should have max_length set to ensure data consistency and prevent potential issues with data storage.",
            }
        return None
