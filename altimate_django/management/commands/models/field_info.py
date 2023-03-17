from dataclasses import dataclass, field, asdict
from typing import List
from django.core.validators import BaseValidator
from django.db.models.fields import Field


@dataclass
class FieldInfo:
    name: str
    model: str
    # add the base object for now to make it easier to work with. Todo: remove this later
    field: Field = None

    def to_dict(self):
        return asdict(self)
