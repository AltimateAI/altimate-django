from django.db import models
from django.test import TestCase
from altimate_django.management.commands.checks.nullable_unique_fields import (
    NullableUniqueFields,
)
from altimate_django.management.commands.models.field_info import FieldInfo


class NullableUniqueFieldsTestModelA(models.Model):
    nullable_unique_field = models.IntegerField(unique=True, null=True)


class NullableUniqueFieldsTestModelB(models.Model):
    non_nullable_unique_field = models.IntegerField(unique=True)


class NullableUniqueFieldsTestModelC(models.Model):
    nullable_non_unique_field = models.IntegerField(null=True)


class TestNullableUniqueFields(TestCase):
    def test_nullable_unique_fields_detected(self):
        fields_to_test = [
            (
                NullableUniqueFieldsTestModelA._meta.get_field("nullable_unique_field"),
                NullableUniqueFieldsTestModelA,
                True,
            ),
            (
                NullableUniqueFieldsTestModelB._meta.get_field(
                    "non_nullable_unique_field"
                ),
                NullableUniqueFieldsTestModelB,
                False,
            ),
            (
                NullableUniqueFieldsTestModelC._meta.get_field(
                    "nullable_non_unique_field"
                ),
                NullableUniqueFieldsTestModelC,
                False,
            ),
        ]

        for field, model, should_detect_issue in fields_to_test:
            field_info = FieldInfo(name=field.name, model=model.__name__, field=field)
            check = NullableUniqueFields(field_info)
            result = check.perform_field_check()

            if should_detect_issue:
                self.assertIsNotNone(
                    result,
                    f"NullableUniqueFields check should detect an issue in {field.name}",
                )
            else:
                self.assertIsNone(
                    result,
                    f"NullableUniqueFields check should not detect an issue in {field.name}",
                )
