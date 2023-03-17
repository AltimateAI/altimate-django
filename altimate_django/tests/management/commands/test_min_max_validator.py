from django.db import models
from django.test import TestCase
from altimate_django.management.commands.checks.minmax_validator import MinMaxValidator
from django.core.validators import MinValueValidator, MaxValueValidator
from altimate_django.management.commands.models.field_info import FieldInfo


class MinMaxValidatorTestModelA(models.Model):
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(150)])


class MinMaxValidatorTestModelB(models.Model):
    age = models.IntegerField(validators=[MinValueValidator(0)])


class MinMaxValidatorTestModelC(models.Model):
    age = models.IntegerField()


class MinMaxValidatorTestCase(TestCase):
    def test_min_max_validator(self):
        # Test a field with both MinValueValidator and MaxValueValidator
        field_info_with_validators = FieldInfo(
            name="age",
            model=MinMaxValidatorTestModelA,
            field=MinMaxValidatorTestModelA._meta.get_field("age"),
        )
        check_with_validators = MinMaxValidator(field_info_with_validators)
        self.assertIsNone(
            check_with_validators.perform_field_check(),
            "MinMaxValidator check should not detect an issue in age field with MinValueValidator and MaxValueValidator",
        )

        # Test a field with only MinValueValidator
        field_info_with_min_validator = FieldInfo(
            name="age",
            model=MinMaxValidatorTestModelB,
            field=MinMaxValidatorTestModelB._meta.get_field("age"),
        )
        check_with_min_validator = MinMaxValidator(field_info_with_min_validator)
        result = check_with_min_validator.perform_field_check()
        self.assertIsNotNone(
            result,
            "MinMaxValidator check should detect an issue in age field with only MinValueValidator",
        )
        self.assertEqual(result["severity"], "Warning")
        self.assertIn(
            "should have MinValueValidator and/or MaxValueValidator",
            result["description"],
        )

        # Test a field without any validators
        field_info_without_validators = FieldInfo(
            name="age",
            model=MinMaxValidatorTestModelC,
            field=MinMaxValidatorTestModelC._meta.get_field("age"),
        )
        check_without_validators = MinMaxValidator(field_info_without_validators)
        result = check_without_validators.perform_field_check()
        self.assertIsNotNone(
            result,
            "MinMaxValidator check should detect an issue in age field without any validators",
        )
        self.assertEqual(result["severity"], "Warning")
        self.assertIn(
            "should have MinValueValidator and/or MaxValueValidator",
            result["description"],
        )
