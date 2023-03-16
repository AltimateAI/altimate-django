from .base_field_check import BaseFieldCheck
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# This check will fail if a ForeignKey or OneToOneField is set to CASCADE
# delete and does not allow null values. This is a best practice, as it
# prevents unintended data loss when related records are deleted.
class MinMaxValidator(BaseFieldCheck):
    def perform_field_check(self):
        field = self.field_info.field
        if isinstance(field, (models.IntegerField, models.DecimalField)):
            min_validator_exists = any(
                isinstance(validator, MinValueValidator)
                for validator in field.validators
            )
            max_validator_exists = any(
                isinstance(validator, MaxValueValidator)
                for validator in field.validators
            )

            if not min_validator_exists or not max_validator_exists:
                return {
                    "severity": "Warning",
                    "description": f"Field {field.name} should have MinValueValidator and/or MaxValueValidator",
                    "explanation": "Adding MinValueValidator and MaxValueValidator to numeric fields can help ensure data consistency and prevent out-of-range values from being stored in the database.",
                }
        return None
