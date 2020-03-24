from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional
from marshmallow_dataclass import class_schema

from .enums import MeasurementType


@dataclass
class Measurement():
    amount: int = field()
    type: MeasurementType = field()
    begin: datetime = field()
    end: datetime = field()
    sector: str = field()
    key: str = field()
    address: Optional[str] = field(default=None)

    @staticmethod
    def get_schema():
        return class_schema(Measurement)(exclude=["address"])


@dataclass
class GGO():
    amount: int = field()
    begin: datetime = field()
    end: datetime = field()
    sector: str = field()
    tech_type: str = field()
    fuel_type: str = field()
    key: str = field()
    address: Optional[str] = field(default=None)

    @staticmethod
    def get_schema():
        return class_schema(GGO)(exclude=["address"])
