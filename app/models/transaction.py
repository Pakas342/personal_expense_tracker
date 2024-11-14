from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
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
    created_at: datetime = Field(default_factory=datetime.now)
    user_id: int = Field(foreign_key="user.id")
    user: User = Relationship(back_populates="transactions")


class TransactionRead(TransactionBase):
    id: int
    created_at: datetime
