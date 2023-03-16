from .base_field_check import BaseFieldCheck
from django.db import models


class ForeignKeyNaming(BaseFieldCheck):
    """
    This class checks if the naming convention for ForeignKey fields in a Django model
    follows the format: "{related_model_name.lower()}_id".

    Inherits from the `BaseFieldCheck` class.
    """

    def perform_field_check(self):
        """
        Checks if the name of the ForeignKey field follows the naming convention.

        Returns:
            dict: A dictionary containing information about the field if the check fails, otherwise None.
        """
        field = self.field_info.field
        if isinstance(field, models.ForeignKey):
            expected_name = f"{field.related_model.__name__.lower()}_id"
            if field.name != expected_name:
                return {
                    "severity": "Low",
                    "description": "Foreign key field name does not follow the naming convention.",
                    "explanation": f"The field '{field.name}' should be named '{expected_name}'.",
                }
        return None
