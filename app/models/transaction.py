from datetime import datetime
from sqlmodel import SQLModel, Field
from enum import Enum


class TransactionType(str, Enum):
    expense = 'expense'
    income = 'income'


class TransactionBase(SQLModel):
    description: str = Field(index=True)
    amount: int = Field(ge=0)
    type: TransactionType


class Transaction(TransactionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class TransactionRead(TransactionBase):
    id: int
    created_at: datetime
