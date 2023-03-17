from .base_field_check import BaseFieldCheck
from django.db import models


class ExcessiveNulls(BaseFieldCheck):
    """
    This class checks if the `null` attribute of non-text fields is set to True,
    which can lead to inconsistent data and complicate handling of missing values.

    Inherits from the `BaseFieldCheck` class.
    """

    def perform_field_check(self):
        """
        Checks if the `null` attribute of the field is set to True for non-text fields.

        Returns:
            dict: A dictionary containing information about the field if the check fails, otherwise None.
        """
        field = self.field_info.field
        if field.null and not isinstance(
            field,
            (models.TextField, models.CharField),
        ):

            return {
                "severity": "Warning",
                "description": f"Field {field.name} has null=True, which might not be necessary",
                "explanation": "Allowing null values for non-text fields can lead to inconsistent data and complicate handling of missing values. Consider removing null=True for fields where null values are not expected or necessary.",
            }

        return None
