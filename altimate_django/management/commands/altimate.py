import pprint
from django.core.management.base import BaseCommand
from django.apps import apps
from tabulate import tabulate
from termcolor import colored
from .models.model_info import ModeInfo
from .models.field_info import FieldInfo
from .checks.reverse_cascade import ReverseCascade
from .checks.minmax_validator import MinMaxValidator
from .checks.excessive_nulls import ExcessiveNulls
from .checks.cascade_for_fk_onetoone import CascadeForFKOneToOne
from .checks.inappropriate_cascade import InappropriateCascade
from .checks.nullable_unique_fields import NullableUniqueFields
from .checks.unbounded_autoincrement_pk import UnboundedAutoIncrementPK
from .checks.cascade_on_foreign_key import CascadeOnForeignKey
from .checks.reserved_sql_keywords import ReservedSQLKeywords
from .checks.foreign_key_naming import ForeignKeyNaming
from .checks.excessive_blanks import ExcessiveBlanks
from .checks.missing_help_text import MissingHelpText
from .checks.large_charfield import LargeCharField
from .checks.unique_without_index import UniqueWithoutIndex
from .checks.missing_default import MissingDefault


FIELD_CHECK_CLASSES = [
    ReverseCascade,
    MinMaxValidator,
    ExcessiveNulls,
    CascadeForFKOneToOne,
    CharFieldsWithoutMaxLength,
    InappropriateCascade,
    MissingRelatedNames,
    NullableUniqueFields,
    CascadeOnDelete,
    UnboundedAutoIncrementPK,
    CascadeOnForeignKey,
    ReservedSQLKeywords,
    ForeignKeyNaming,
    ExcessiveBlanks,
    MissingHelpText,
    LargeCharField,
    UniqueWithoutIndex,
    MissingDefault,
    RelatedName,
]


class Command(BaseCommand):
    help = "Prints the schema of all models and their entity relationship"

    severity_colors = {
        "High": "red",
        "Warning": "yellow",
        "Low": "cyan",
    }

    def collect_check_data(self, model):
        return ModeInfo(
            model_name=model.__name__,
            object_count=model.objects.count(),
            has__str__=hasattr(model, "__str__"),
            has__unicode__=hasattr(model, "__unicode__"),
            fields=[
                self.create_field_schema(model, field)
                for field in model._meta.get_fields()
            ],
        )

    def create_field_schema(self, model, field):
        field_schema_args = {
            "name": field.name,
            "model": model.__name__,
            "field": field,
        }

        return FieldInfo(**field_schema_args)

    def fetch_schema(self):
        model_schemas = [
            ModeInfo(
                model_name=model.__name__,
                fields=[
                    self.create_field_schema(model, field)
                    for field in model._meta.get_fields()
                ],
            )
            for model in apps.get_models()
        ]

        schema_list = [model_schema.to_dict() for model_schema in model_schemas]
        pp = pprint.PrettyPrinter(width=38, compact=True)
        pp.pprint(schema_list)

    def check_data_issues(self, model_info: ModeInfo):
        recommendations = []
        for field_info in model_info.fields:
            for check in FIELD_CHECK_CLASSES:
                result = check(field_info).perform_field_check()
                if result:
                    recommendations.append(
                        (model_info.model_name, field_info.name, result)
                    )
        return recommendations

    def create_table_data(self, recommendations):

        table_data = []
        for model_name, field_name, recommendation in recommendations:
            if field_name and recommendation:
                severity, description, explanation = (
                    recommendation["severity"],
                    recommendation["description"],
                    recommendation["explanation"],
                )
                color = self.severity_colors.get(severity, "green")

                table_data.append(
                    [
                        f"{model_name}.{field_name}",
                        colored(severity, color),
                        description,
                        explanation,
                    ]
                )
        return table_data

    def handle(self, *args, **options):
        recommendations = []

        for model in apps.get_models():
            model_info = self.collect_check_data(model)
            recommendations.extend(self.check_data_issues(model_info))

        if recommendations:
            self.stdout.write("Data Issues Detected:")

            headers = ["Model.Field", "Severity", "Description", "Explanation"]
            table_data = self.create_table_data(recommendations)

            table_str = tabulate(
                table_data,
                headers=headers,
                tablefmt="grid",
                maxcolwidths=[None, None, 60, 60],
            )
            self.stdout.write(table_str)

        else:
            self.stdout.write("No data issues detected.")
