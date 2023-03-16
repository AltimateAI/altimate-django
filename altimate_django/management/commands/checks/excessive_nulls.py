from .base_field_check import BaseFieldCheck
from django.db import models


class ExcessiveNulls(BaseFieldCheck):
    """
    Checks that non-text fields do not have null=True.
    """

    def perform_field_check(self):
        field = self.field_info.field
        if field.null and not isinstance(
            field,
            (
                models.TextField,
                models.CharField,
                models.DecimalField,
                models.IntegerField,
            ),
        ):

            return {
                "severity": "Warning",
                "description": f"Field {field.name} has null=True, which might not be necessary",
                "explanation": "Allowing null values for non-text fields can lead to inconsistent data and complicate handling of missing values. Consider removing null=True for fields where null values are not expected or necessary.",
            }

        return None
