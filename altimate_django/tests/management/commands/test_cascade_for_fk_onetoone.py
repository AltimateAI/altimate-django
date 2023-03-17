from django.db import models
from django.test import TestCase
from altimate_django.management.commands.checks.cascade_for_fk_onetoone import (
    CascadeForFKOneToOne,
)
from altimate_django.management.commands.models.field_info import FieldInfo


class FKTestModelA(models.Model):
    pass


class FKTestModelB(models.Model):
    cascade_field = models.ForeignKey(
        FKTestModelA, on_delete=models.CASCADE, related_name="cascade_test_model_bs"
    )
    set_null_field = models.ForeignKey(
        FKTestModelA,
        on_delete=models.SET_NULL,
        null=True,
        related_name="set_null_test_model_bs",
    )
    protect_field = models.ForeignKey(
        FKTestModelA, on_delete=models.PROTECT, related_name="protect_test_model_bs"
    )


class FKTestModelC(models.Model):
    one_to_one_cascade = models.OneToOneField(
        FKTestModelA,
        on_delete=models.CASCADE,
        related_name="one_to_one_cascade_test_model_c",
    )
    one_to_one_protect = models.OneToOneField(
        FKTestModelA,
        on_delete=models.PROTECT,
        related_name="one_to_one_protect_test_model_c",
    )


class TestCascadeForFKOneToOne(TestCase):
    def test_cascade_on_foreign_key(self):
        field_info = FieldInfo(
            field=FKTestModelB._meta.get_field("cascade_field"),
            name="cascade_field",
            model=FKTestModelB,
        )
        check = CascadeForFKOneToOne(field_info)
        result = check.perform_field_check()
        self.assertIsNone(
            result,
            "CascadeForFKOneToOne check should not detect an issue with CASCADE behavior",
        )

    def test_non_cascade_on_foreign_key(self):
        field_info = FieldInfo(
            field=FKTestModelB._meta.get_field("set_null_field"),
            name="cascade_field",
            model=FKTestModelB,
        )
        check = CascadeForFKOneToOne(field_info)
        result = check.perform_field_check()
        self.assertIsNotNone(
            result,
            "CascadeForFKOneToOne check should detect an issue with non-CASCADE behavior",
        )

    def test_non_cascade_on_one_to_one(self):
        field_info = FieldInfo(
            field=FKTestModelC._meta.get_field("one_to_one_protect"),
            name="cascade_field",
            model=FKTestModelC,
        )
        check = CascadeForFKOneToOne(field_info)
        result = check.perform_field_check()
        self.assertIsNotNone(
            result,
            "CascadeForFKOneToOne check should detect an issue with non-CASCADE behavior",
        )
