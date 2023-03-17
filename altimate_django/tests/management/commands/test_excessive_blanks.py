from django.test import TestCase
from django.db import models
from django.db import models
from altimate_django.management.commands.checks.excessive_blanks import ExcessiveBlanks
from altimate_django.management.commands.models.field_info import FieldInfo


class ExcessiveBlanksTestModelA(models.Model):
    no_blank = models.CharField(max_length=255)
    excessive_blank = models.CharField(max_length=255, blank=True)


class ExcessiveBlanksTestExcessiveBlanks(TestCase):
    def test_no_blank(self):
        field_info = FieldInfo(
            field=ExcessiveBlanksTestModelA._meta.get_field("no_blank"),
            name="no_blank",
            model=ExcessiveBlanksTestModelA,
        )
        check = ExcessiveBlanks(field_info)
        result = check.perform_field_check()
        self.assertIsNone(result)

    def test_excessive_blank(self):
        field_info = FieldInfo(
            field=ExcessiveBlanksTestModelA._meta.get_field("excessive_blank"),
            name="excessive_blank",
            model=ExcessiveBlanksTestModelA,
        )
        check = ExcessiveBlanks(field_info)
        result = check.perform_field_check()
        expected_result = {
            "field_name": "excessive_blank",
            "severity": "Info",
            "description": "Excessive use of blank=True",
            "explanation": "Using blank=True excessively may cause issues with data consistency and validation. Review your use of blank=True in this field and consider removing it if it's not necessary.",
        }
        self.assertEqual(result, expected_result)
