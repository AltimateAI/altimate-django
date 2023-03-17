from django.db import models
from django.test import TestCase
from altimate_django.management.commands.checks.inappropriate_cascade import (
    InappropriateCascade,
)
from altimate_django.management.commands.models.field_info import FieldInfo


class InappropriateCascadeTestModelC(models.Model):
    pass


class InappropriateCascadeTestModelD(models.Model):
    cascade_field = models.ForeignKey(
        InappropriateCascadeTestModelC,
        on_delete=models.CASCADE,
        related_name="cascade_related",
    )
    set_null_field = models.ForeignKey(
        InappropriateCascadeTestModelC,
        on_delete=models.SET_NULL,
        null=True,
        related_name="set_null_related",
    )


class InappropriateCascadeTestCase(TestCase):
    def test_inappropriate_cascade(self):
        # Test a ForeignKey with CASCADE on_delete
        field_info_cascade = FieldInfo(
            name="cascade_field",
            model=InappropriateCascadeTestModelD,
            field=InappropriateCascadeTestModelD._meta.get_field("cascade_field"),
        )
        check_cascade = InappropriateCascade(field_info_cascade)
        result_cascade = check_cascade.perform_field_check()
        self.assertIsNotNone(
            result_cascade,
            "InappropriateCascade check should detect an issue in cascade_field",
        )
        self.assertEqual(result_cascade["severity"], "Medium")
        self.assertIn(
            "Inappropriate use of CASCADE on ForeignKey", result_cascade["description"]
        )

        # Test a ForeignKey with SET_NULL on_delete
        field_info_set_null = FieldInfo(
            name="set_null_field",
            model=InappropriateCascadeTestModelD,
            field=InappropriateCascadeTestModelD._meta.get_field("set_null_field"),
        )
        check_set_null = InappropriateCascade(field_info_set_null)
        self.assertIsNone(
            check_set_null.perform_field_check(),
            "InappropriateCascade check should not detect an issue in set_null_field",
        )
