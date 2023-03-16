# data_issues_detector/checks/base_check.py
from abc import ABC, abstractmethod


class BaseCheck(ABC):
    def __init__(self, model, field):
        self.model = model
        self.field = field

    @abstractmethod
    def perform_field_check(self):
        pass
