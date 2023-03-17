from django.db import models
from django.test import TestCase
from altimate_django.management.commands.checks.missing_default import MissingDefault
from altimate_django.management.commands.models.field_info import FieldInfo


class MissingDefaultTestModelA(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, default="No description")
    created_at = models.DateTimeField(auto_now_add=True)


class MissingDefaultTestModelB(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField()


class MissingDefaultTestCase(TestCase):
    def test_missing_default(self):
        # Test a field with a default value
        field_info_with_default = FieldInfo(
            name="description",
            model=MissingDefaultTestModelA,
            field=MissingDefaultTestModelA._meta.get_field("description"),
        )
        check_with_default = MissingDefault(field_info_with_default)
        self.assertIsNone(
            check_with_default.perform_field_check(),
            "MissingDefault check should not detect an issue in description field with default value",
        )

        # Test a field without a default value
        field_info_without_default = FieldInfo(
            name="description",
            model=MissingDefaultTestModelB,
            field=MissingDefaultTestModelB._meta.get_field("description"),
        )
        check_without_default = MissingDefault(field_info_without_default)
        result = check_without_default.perform_field_check()
        self.assertIsNotNone(
            result,
            "MissingDefault check should detect an issue in description field without default value",
        )
        self.assertEqual(result["severity"], "Warning")
        self.assertIn(
            "should have a default value or be nullable", result["description"]
        )

        # Test a DateTimeField with auto_now_add
        field_info_with_auto_now_add = FieldInfo(
            name="created_at",
            model=MissingDefaultTestModelA,
            field=MissingDefaultTestModelA._meta.get_field("created_at"),
        )
        check_with_auto_now_add = MissingDefault(field_info_with_auto_now_add)
        self.assertIsNone(
            check_with_auto_now_add.perform_field_check(),
            "MissingDefault check should not detect an issue in DateTimeField with auto_now_add",
        )

        # Test a DateTimeField without auto_now_add or default value
        field_info_without_auto_now_add = FieldInfo(
            name="created_at",
            model=MissingDefaultTestModelB,
            field=MissingDefaultTestModelB._meta.get_field("created_at"),
        )
        check_without_auto_now_add = MissingDefault(field_info_without_auto_now_add)
        result = check_without_auto_now_add.perform_field_check()
        self.assertIsNotNone(
            result,
            "MissingDefault check should detect an issue in DateTimeField without auto_now_add and default value",
        )
        self.assertEqual(result["severity"], "Warning")
        self.assertIn(
            "should have a default value or be nullable", result["description"]
        )
