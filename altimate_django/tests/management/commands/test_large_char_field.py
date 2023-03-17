from django.db import models
from django.test import TestCase
from altimate_django.management.commands.checks.large_charfield import LargeCharField
from altimate_django.management.commands.models.field_info import FieldInfo


class LargeCharFieldTestModelA(models.Model):
    normal_charfield = models.CharField(max_length=100)


class LargeCharFieldTestModelB(models.Model):
    large_charfield = models.CharField(max_length=500)


class LargeCharFieldTestCase(TestCase):
    def test_large_char_field(self):
        # Test a CharField with a max_length below the threshold
        field_info_normal_charfield = FieldInfo(
            name="normal_charfield",
            model=LargeCharFieldTestModelA,
            field=LargeCharFieldTestModelA._meta.get_field("normal_charfield"),
        )
        check_normal_charfield = LargeCharField(field_info_normal_charfield)
        self.assertIsNone(
            check_normal_charfield.perform_field_check(),
            "LargeCharField check should not detect an issue in normal_charfield",
        )

        # Test a CharField with a max_length above the threshold
        field_info_large_charfield = FieldInfo(
            name="large_charfield",
            model=LargeCharFieldTestModelB,
            field=LargeCharFieldTestModelB._meta.get_field("large_charfield"),
        )
        check_large_charfield = LargeCharField(field_info_large_charfield)
        result = check_large_charfield.perform_field_check()
        self.assertIsNotNone(
            result, "LargeCharField check should detect an issue in large_charfield"
        )
        self.assertEqual(result["severity"], "Warning")
        self.assertIn(
            "Consider using TextField instead of CharField", result["description"]
        )
