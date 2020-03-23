from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List
from marshmallow import validate, validates_schema, ValidationError

from .enums import MeasurementType

@dataclass
class LedgerPublishMeasurementRequest:
    begin: datetime = field()   
    end: datetime = field()
    sector: str = field(metadata={"validate": validate.OneOf(['DK1', 'DK2'])})
    type: MeasurementType = field()
    amount: int = field(metadata={"validate": validate.Range(min=0)})
    key: str = field()

    @validates_schema
    def validate_numbers(self, data, **kwargs):
        
        if  data['begin'] >= data['end']:
            raise ValidationError('Begin must be before End!')

        if (data['end'] - data['begin']) != timedelta(hours=1):
            raise ValidationError('Only positive hourly measurements are currently supported!')



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

