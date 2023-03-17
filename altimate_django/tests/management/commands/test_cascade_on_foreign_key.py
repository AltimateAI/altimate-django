from django.test import TestCase
from django.db import models
from django.db import models
from altimate_django.management.commands.checks.cascade_on_foreign_key import (
    CascadeOnForeignKey,
)
from altimate_django.management.commands.models.field_info import FieldInfo


class CascadeOnForeignKeyTestModelA(models.Model):
    pass


class CascadeOnForeignKeyTestModelB(models.Model):
    cascade_field = models.ForeignKey(
        CascadeOnForeignKeyTestModelA,
        on_delete=models.CASCADE,
        related_name="cascade_related",
    )
    set_null_field = models.ForeignKey(
        CascadeOnForeignKeyTestModelA,
        on_delete=models.SET_NULL,
        null=True,
        related_name="set_null_related",
    )
    protect_field = models.ForeignKey(
        CascadeOnForeignKeyTestModelA,
        on_delete=models.PROTECT,
        related_name="protect_related",
    )


class TestCascadeOnForeignKey(TestCase):
    def test_cascade_on_foreign_key(self):
        field_info = FieldInfo(
            field=CascadeOnForeignKeyTestModelB._meta.get_field("cascade_field"),
            name="cascade_field",
            model=CascadeOnForeignKeyTestModelB,
        )
        check = CascadeOnForeignKey(field_info)
        result = check.perform_field_check()
        self.assertIsNotNone(result)

    def test_set_null_on_foreign_key(self):
        field_info = FieldInfo(
            field=CascadeOnForeignKeyTestModelB._meta.get_field("set_null_field"),
            name="set_null_field",
            model=CascadeOnForeignKeyTestModelB,
        )
        check = CascadeOnForeignKey(field_info)
        result = check.perform_field_check()
        self.assertIsNone(result)

    def test_protect_on_foreign_key(self):
        field_info = FieldInfo(
            field=CascadeOnForeignKeyTestModelB._meta.get_field("protect_field"),
            name="protect_field",
            model=CascadeOnForeignKeyTestModelB,
        )
        check = CascadeOnForeignKey(field_info)
        result = check.perform_field_check()
        self.assertIsNone(result)
