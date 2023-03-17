from django.db import models
from django.test import TestCase
from altimate_django.management.commands.checks.reverse_cascade import ReverseCascade
from altimate_django.management.commands.models.field_info import FieldInfo


class RelatedModel(models.Model):
    pass


class TestModelA(models.Model):
    related_model = models.ForeignKey(RelatedModel, on_delete=models.CASCADE)


class TestModelB(models.Model):
    related_model = models.OneToOneField(RelatedModel, on_delete=models.CASCADE)


class TestModelC(models.Model):
    related_model = models.ForeignKey(RelatedModel, on_delete=models.CASCADE, null=True)


class TestModelD(models.Model):
    related_model = models.ForeignKey(RelatedModel, on_delete=models.PROTECT)


class TestReverseCascade(TestCase):
    def test_reverse_cascade_detected(self):
        fields_to_test = [
            (TestModelA._meta.get_field("related_model"), TestModelA, True),
            (TestModelB._meta.get_field("related_model"), TestModelB, True),
            (TestModelC._meta.get_field("related_model"), TestModelC, False),
            (TestModelD._meta.get_field("related_model"), TestModelD, False),
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
