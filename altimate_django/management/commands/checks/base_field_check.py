# data_issues_detector/checks/base_check.py
from abc import ABC, abstractmethod

from ..models.field_info import FieldInfo


class BaseFieldCheck(ABC):
    def __init__(self, field_info: FieldInfo):
        self.field_info = field_info

    @abstractmethod
    def perform_field_check(self):
        pass
