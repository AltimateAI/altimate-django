from django.test import TestCase
from django.db import models
from django.db import models
from altimate_django.management.commands.checks.unique_without_index import (
    UniqueWithoutIndex,
)
from altimate_django.management.commands.models.field_info import FieldInfo


class TestModelA(models.Model):
    field1 = models.CharField(max_length=100, unique=True, db_index=True)


class TestModelB(models.Model):
    field2 = models.CharField(max_length=100, unique=True, db_index=False)


class TestModelC(models.Model):
    field3 = models.CharField(max_length=100, unique=False, db_index=True)


class TestModelD(models.Model):
    field4 = models.CharField(max_length=100, unique=False, db_index=False)


class TestUniqueWithoutIndex(TestCase):
    def test_unique_without_index_detected(self):
        fields_to_test = [
            (TestModelA._meta.get_field("field1"), TestModelA, False),
            (TestModelB._meta.get_field("field2"), TestModelB, True),
            (TestModelC._meta.get_field("field3"), TestModelC, False),
            (TestModelD._meta.get_field("field4"), TestModelD, False),
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
