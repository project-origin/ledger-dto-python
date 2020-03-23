from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional

from .enums import MeasurementType


@dataclass
class Measurement():
    address: Optional[str] = field()
    amount: int = field()
    type: MeasurementType = field()
    begin: datetime = field()
    end: datetime = field()
    sector: str = field()
    key: str = field()


@dataclass
class GGO():
    address: Optional[str] = field()
    amount: int = field()
    begin: datetime = field()
    end: datetime = field()
    sector: str = field()
    tech_type: str = field()
    fuel_type: str = field()
    key: str = field()
