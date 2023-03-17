from django.test import TestCase
from django.db import models
from django.db import models
from altimate_django.management.commands.checks.excessive_nulls import ExcessiveNulls
from altimate_django.management.commands.models.field_info import FieldInfo


class ExcessiveNullsTestModelA(models.Model):
    char_field = models.CharField(max_length=100, null=True)
    int_field = models.IntegerField(null=True)


class ExcessiveNullsTestModelB(models.Model):
    char_field = models.CharField(max_length=100)
    int_field = models.IntegerField()


class ExcessiveNullsTestCase(TestCase):
    def test_excessive_nulls_detected(self):
        fields_to_test = [
            ("int_field", True),
        ]

        for field_name, should_detect in fields_to_test:
            field = ExcessiveNullsTestModelA._meta.get_field(field_name)
            field_info = FieldInfo(
                name=field_name, model=ExcessiveNullsTestModelA, field=field
            )
            excessive_nulls_check = ExcessiveNulls(field_info)
            result = excessive_nulls_check.perform_field_check()
            if should_detect:
                self.assertIsNotNone(
                    result,
                    f"ExcessiveNulls check should detect an issue in {field_name}",
                )
            else:
                self.assertIsNone(
                    result,
                    f"ExcessiveNulls check should not detect any issue in {field_name}",
                )

    def test_excessive_nulls_not_detected(self):
        fields_to_test = [
            ("char_field", False),
        ]

        for field_name, should_detect in fields_to_test:
            field = ExcessiveNullsTestModelB._meta.get_field(field_name)
            field_info = FieldInfo(
                name=field_name, model=ExcessiveNullsTestModelB, field=field
            )
            excessive_nulls_check = ExcessiveNulls(field_info)
            result = excessive_nulls_check.perform_field_check()

            if should_detect:
                self.assertIsNone(
                    result,
                    f"ExcessiveNulls check should detect an issue in {field_name}",
                )
            else:
                self.assertIsNone(
                    result,
                    f"ExcessiveNulls check should not detect any issue in {field_name}",
                )
