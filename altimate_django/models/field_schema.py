from dataclasses import dataclass, field, asdict


@dataclass
class FieldSchema:
    name: str
    model: str
    field_type: str
    related_model: str = None
    on_delete: str = None
    related_name: str = None
    related_query_name: str = None
    through: str = None
    max_length: int = None
    max_digits: int = None
    decimal_places: int = None
    max_value: int = None
    min_value: int = None
    default: str = None
    auto_now: bool = None
    auto_now_add: bool = None
    upload_to: str = None
    allow_unicode: bool = None
    verify_exists: bool = None
    null: bool = None
    auto_created: bool = None
    blank: bool = None
    help_text: str = None

    def to_dict(self):
        return asdict(self)
