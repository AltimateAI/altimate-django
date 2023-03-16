from dataclasses import dataclass, field, asdict
from typing import List

from .field_info import FieldInfo


@dataclass
class ModeInfo:
    model_name: str
    object_count: int
    has__str__: bool
    has__unicode__: bool
    fields: List[FieldInfo] = field(default_factory=list)

    def to_dict(self):
        return {
            "model_name": self.model_name,
            "fields": [field.to_dict() for field in self.fields],
        }
