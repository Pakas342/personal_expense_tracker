from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

# This is done because even tho SQLmodel on runtime uses lazy imports, on compiling the type checkers as pydantic need
# to solve the import right away
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
    # SQLmodel does what's call a lazy import, where it doesn't resolves the input right away, but waits until being
    # called to try to resolve it. This gives a window to load the other models in runtime
    user: "User" = Relationship(back_populates="transactions")


class TransactionRead(TransactionBase):
    id: int
    created_at: datetime
    user_id: int | None
