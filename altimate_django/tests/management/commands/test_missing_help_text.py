from django.db import models
from django.test import TestCase
from altimate_django.management.commands.checks.missing_help_text import MissingHelpText
from altimate_django.management.commands.models.field_info import FieldInfo


class MissingHelpTextTestModelA(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(
        max_length=100, help_text="A short description of the model."
    )


class MissingHelpTextTestModelB(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


class MissingHelpTextTestCase(TestCase):
    def test_missing_help_text(self):
        # Test a field with help_text
        field_info_with_help_text = FieldInfo(
            name="description",
            model=MissingHelpTextTestModelA,
            field=MissingHelpTextTestModelA._meta.get_field("description"),
        )
        check_with_help_text = MissingHelpText(field_info_with_help_text)
        self.assertIsNone(
            check_with_help_text.perform_field_check(),
            "MissingHelpText check should not detect an issue in description field with help_text",
        )

        # Test a field without help_text
        field_info_without_help_text = FieldInfo(
            name="description",
            model=MissingHelpTextTestModelB,
            field=MissingHelpTextTestModelB._meta.get_field("description"),
        )
        check_without_help_text = MissingHelpText(field_info_without_help_text)
        result = check_without_help_text.perform_field_check()
        self.assertIsNotNone(
            result,
            "MissingHelpText check should detect an issue in description field without help_text",
        )
        self.assertEqual(result["severity"], "Low")
        self.assertIn("does not have help_text", result["description"])
