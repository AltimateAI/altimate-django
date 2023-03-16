from dataclasses import dataclass, field
from typing import List

from .field_schema import FieldSchema


@dataclass
class ModelSchema:
    model_name: str
    fields: List[FieldSchema] = field(default_factory=list)

    def to_dict(self):
        return {
            "model_name": self.model_name,
            "fields": [field.to_dict() for field in self.fields],
        }
