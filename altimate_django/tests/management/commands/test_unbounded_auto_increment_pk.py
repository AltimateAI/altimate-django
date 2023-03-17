from django.test import TestCase
from django.db import models
from django.db import models
from altimate_django.management.commands.checks.unbounded_autoincrement_pk import (
    UnboundedAutoIncrementPK,
)
from altimate_django.management.commands.models.field_info import FieldInfo


class TestModelA(models.Model):
    id = models.AutoField(primary_key=True)


class TestModelB(models.Model):
    id = models.AutoField(primary_key=True, max_length=11)


class TestModelC(models.Model):
    id = models.BigAutoField(primary_key=True)


class TestUnboundedAutoIncrementPK(TestCase):
    def test_unbounded_auto_increment_pk_detected(self):
        fields_to_test = [
            (TestModelA._meta.get_field("id"), TestModelA, True),
            (TestModelB._meta.get_field("id"), TestModelB, False),
            (TestModelC._meta.get_field("id"), TestModelC, True),
        ]

        for field, model, should_detect_issue in fields_to_test:
            field_info = FieldInfo(name=field.name, model=model.__name__, field=field)
            check = UnboundedAutoIncrementPK(field_info)
            result = check.perform_field_check()

            if should_detect_issue:
                self.assertIsNotNone(
                    result,
                    f"UnboundedAutoIncrementPK check should detect an issue in {field.name}",
                )
            else:
                self.assertIsNone(
                    result,
                    f"UnboundedAutoIncrementPK check should not detect an issue in {field.name}",
                )
