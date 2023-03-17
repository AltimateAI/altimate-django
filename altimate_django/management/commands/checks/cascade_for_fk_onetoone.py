from .base_field_check import BaseFieldCheck
from django.db import models


class CascadeForFKOneToOne(BaseFieldCheck):
    """
    A class used to check if ForeignKey or OneToOneField fields are using
    the CASCADE option for on_delete. Inherits from the BaseFieldCheck class.

    Attributes
    ----------
    field_info : FieldInfo
        The information of the field to be checked.

    Methods
    -------
    perform_field_check():
        Checks if the field is of ForeignKey or OneToOneField type and if
        it's using the CASCADE option for on_delete. Returns a dictionary
        with relevant information if the check fails, otherwise returns None.
    """

    def perform_field_check(self):
        """
        Checks if the field is of ForeignKey or OneToOneField type and if
        it's using the CASCADE option for on_delete.

        Returns
        -------
        dict or None
            If the check fails, returns a dictionary with the field name,
            severity, description, and explanation. Otherwise, returns None.
        """

        if (
            isinstance(
                self.field_info.field,
                (models.ForeignKey, models.OneToOneField),
            )
            and self.field_info.field.remote_field.on_delete != models.CASCADE
        ):
            return {
                "field_name": self.field_info.name,
                "severity": "Medium",
                "description": "Non-CASCADE option used for ForeignKey or OneToOneField",
                "explanation": "ForeignKey and OneToOneField fields should use on_delete=models.CASCADE to ensure database integrity.",
            }
        return None
