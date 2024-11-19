from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.user import User


class TransactionType(str, Enum):
    expense = 'expense'
    income = 'income'


class TransactionBase(SQLModel):
    description: str = Field(index=True)
    amount: float = Field(ge=0)
    type: TransactionType


class Transaction(TransactionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)
    user_id: int = Field(foreign_key="user.id")
    user: "User" = Relationship(back_populates="transactions")


class TransactionRead(TransactionBase):
    id: int
    created_at: datetime
