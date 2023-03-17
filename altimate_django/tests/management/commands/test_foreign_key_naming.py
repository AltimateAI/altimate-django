from django.db import models
from django.test import TestCase
from altimate_django.management.commands.checks.foreign_key_naming import (
    ForeignKeyNaming,
)
from altimate_django.management.commands.models.field_info import FieldInfo


class RelatedModel(models.Model):
    name = models.CharField(max_length=255)


class TestModelA(models.Model):
    relatedmodel_id = models.ForeignKey(RelatedModel, on_delete=models.CASCADE)


class TestModelB(models.Model):
    incorrect_related_name = models.ForeignKey(RelatedModel, on_delete=models.CASCADE)


class TestForeignKeyNaming(TestCase):
    def test_correct_naming_convention(self):
        field_info = FieldInfo(
            field=TestModelA._meta.get_field("relatedmodel_id"),
            name="relatedmodel_id",
            model=TestModelA,
        )
        check = ForeignKeyNaming(field_info)
        result = check.perform_field_check()
        self.assertIsNone(result)

    def test_incorrect_naming_convention(self):
        field_info = FieldInfo(
            field=TestModelB._meta.get_field("incorrect_related_name"),
            name="incorrect_related_name",
            model=TestModelB,
        )
        check = ForeignKeyNaming(field_info)
        result = check.perform_field_check()
        self.assertIsNotNone(result)
        self.assertEqual(
            result["explanation"],
            "The field 'incorrect_related_name' should be named 'relatedmodel_id'.",
        )
