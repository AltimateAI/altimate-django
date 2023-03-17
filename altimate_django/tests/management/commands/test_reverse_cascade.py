from django.db import models
from django.test import TestCase
from altimate_django.management.commands.checks.reverse_cascade import ReverseCascade
from altimate_django.management.commands.models.field_info import FieldInfo


class ReverseCascadeRelatedModel(models.Model):
    pass


class ReverseCascadeTestModelA(models.Model):
    related_model = models.ForeignKey(
        ReverseCascadeRelatedModel, on_delete=models.CASCADE
    )


class ReverseCascadeTestModelB(models.Model):
    related_model = models.OneToOneField(
        ReverseCascadeRelatedModel, on_delete=models.CASCADE
    )


class ReverseCascadeTestModelC(models.Model):
    related_model = models.ForeignKey(
        ReverseCascadeRelatedModel, on_delete=models.CASCADE, null=True
    )


class ReverseCascadeTestModelD(models.Model):
    related_model = models.ForeignKey(
        ReverseCascadeRelatedModel, on_delete=models.PROTECT
    )


class TestReverseCascade(TestCase):
    def test_reverse_cascade_detected(self):
        fields_to_test = [
            (
                ReverseCascadeTestModelA._meta.get_field("related_model"),
                ReverseCascadeTestModelA,
                True,
            ),
            (
                ReverseCascadeTestModelB._meta.get_field("related_model"),
                ReverseCascadeTestModelB,
                True,
            ),
            (
                ReverseCascadeTestModelC._meta.get_field("related_model"),
                ReverseCascadeTestModelC,
                False,
            ),
            (
                ReverseCascadeTestModelD._meta.get_field("related_model"),
                ReverseCascadeTestModelD,
                False,
            ),
        ]

        for field, model, should_detect_issue in fields_to_test:
            field_info = FieldInfo(name=field.name, model=model.__name__, field=field)
            check = ReverseCascade(field_info)
            result = check.perform_field_check()

            if should_detect_issue:
                self.assertIsNotNone(
                    result,
                    f"ReverseCascade check should detect an issue in {field.name}",
                )
            else:
                self.assertIsNone(
                    result,
                    f"ReverseCascade check should not detect an issue in {field.name}",
                )
