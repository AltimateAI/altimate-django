from django.db import models
from django.test import TestCase
from altimate_django.management.commands.checks.cascade_for_fk_onetoone import (
    CascadeForFKOneToOne,
)
from altimate_django.management.commands.models.field_info import FieldInfo


class ParentModel(models.Model):
    name = models.CharField(max_length=100)


class TestModelA(models.Model):
    parent = models.ForeignKey(ParentModel, on_delete=models.CASCADE)


class TestModelB(models.Model):
    parent = models.ForeignKey(ParentModel, on_delete=models.PROTECT)


class TestModelC(models.Model):
    parent = models.OneToOneField(ParentModel, on_delete=models.CASCADE)


class TestModelD(models.Model):
    parent = models.OneToOneField(ParentModel, on_delete=models.PROTECT)


class TestCascadeForFKOneToOne(TestCase):
    def test_cascade_for_fk_onetoone_detected(self):
        fields_to_test = [
            (TestModelA._meta.get_field("parent"), TestModelA, True),
            (TestModelB._meta.get_field("parent"), TestModelB, False),
            (TestModelC._meta.get_field("parent"), TestModelC, True),
            (TestModelD._meta.get_field("parent"), TestModelD, False),
        ]

        for field, model, should_detect_issue in fields_to_test:
            field_info = FieldInfo(name=field.name, model=model.__name__, field=field)
            check = CascadeForFKOneToOne(field_info)
            result = check.perform_field_check()

            if should_detect_issue:
                self.assertIsNotNone(
                    result,
                    f"CascadeForFKOneToOne check should detect an issue in {field.name}",
                )
            else:
                self.assertIsNone(
                    result,
                    f"CascadeForFKOneToOne check should not detect an issue in {field.name}",
                )
