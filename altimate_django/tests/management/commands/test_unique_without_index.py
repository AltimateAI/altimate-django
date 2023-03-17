from django.test import TestCase
from django.db import models
from django.db import models
from altimate_django.management.commands.checks.unique_without_index import (
    UniqueWithoutIndex,
)
from altimate_django.management.commands.models.field_info import FieldInfo


class UniqueWithoutIndexTestModelA(models.Model):
    field1 = models.CharField(max_length=100, unique=True, db_index=True)


class UniqueWithoutIndexTestModelB(models.Model):
    field2 = models.CharField(max_length=100, unique=True, db_index=False)


class UniqueWithoutIndexTestModelC(models.Model):
    field3 = models.CharField(max_length=100, unique=False, db_index=True)


class UniqueWithoutIndexTestModelD(models.Model):
    field4 = models.CharField(max_length=100, unique=False, db_index=False)


class TestUniqueWithoutIndex(TestCase):
    def test_unique_without_index_detected(self):
        fields_to_test = [
            (
                UniqueWithoutIndexTestModelA._meta.get_field("field1"),
                UniqueWithoutIndexTestModelA,
                False,
            ),
            (
                UniqueWithoutIndexTestModelB._meta.get_field("field2"),
                UniqueWithoutIndexTestModelB,
                True,
            ),
            (
                UniqueWithoutIndexTestModelC._meta.get_field("field3"),
                UniqueWithoutIndexTestModelC,
                False,
            ),
            (
                UniqueWithoutIndexTestModelD._meta.get_field("field4"),
                UniqueWithoutIndexTestModelD,
                False,
            ),
        ]

        for field, model, should_detect_issue in fields_to_test:
            field_info = FieldInfo(name=field.name, model=model.__name__, field=field)
            check = UniqueWithoutIndex(field_info)
            result = check.perform_field_check()

            if should_detect_issue:
                self.assertIsNotNone(
                    result,
                    f"UniqueWithoutIndex check should detect an issue in {field.name}",
                )
            else:
                self.assertIsNone(
                    result,
                    f"UniqueWithoutIndex check should not detect an issue in {field.name}",
                )
