from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import List


class UserBase(SQLModel):
    email: str = Field(index=True)
    password: str = Field()


class User(UserBase, table=True):
    id: int | None = Field(primary_key=True, default=None)
    created_at: datetime = Field(default_factory=datetime.now)
    transactions: List["Transaction"] = Relationship(back_populates="user")


class UserRead(UserBase):
    id: int
    created_at: datetime
    transactions: List["Transaction"] | None

