from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from .enums import MeasurementType

@dataclass
class LedgerPublishMeasurementRequest:
    begin: datetime = field()   
    end: datetime = field()
    sector: str = field()
    type: MeasurementType = field()
    amount: int = field()
    key: str = field()


@dataclass
class LedgerIssueGGORequest:
    origin: str = field()
    tech_type: str = field()
    fuel_type: str = field()
    key: str = field()


@dataclass
class LedgerTransferGGORequest:
    key: str = field()
    

@dataclass
class LedgerRetireGGORequest:
    settlement_address: str = field()

@dataclass
class LedgerSettlementRequest:
    measurement_address: str = field()
    settlement_address: str = field()
    ggo_addresses: List[str] = field()


@dataclass
class LedgerSplitGGOPart:
    address: str = field()
    amount: int = field()
    key: str = field()

@dataclass
class LedgerSplitGGORequest:
    parts: List[LedgerSplitGGOPart] = field()

