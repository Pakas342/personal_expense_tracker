from datetime import datetime
from typing import List
from typing import TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

# Had to take this outside of the typechecking because this is not a SQLmodel, but a pydantic data class,
# and pydantic requires the data classes to be solved right away on runtime
from app.models.transaction import TransactionRead

# This is done because even tho SQLmodel on runtime uses lazy imports, on compiling the type checkers as pydantic need
# to solve the import right away
if TYPE_CHECKING:
    from app.models.transaction import Transaction


class UserBase(SQLModel):
    email: str = Field(index=True)
    password: str = Field()


class User(UserBase, table=True):
    id: int | None = Field(primary_key=True, default=None)
    created_at: datetime = Field(default_factory=datetime.now)
    # SQLmodel does what's call a lazy import, where it doesn't resolves the input right away, but waits until being
    # called to try to resolve it. This gives a window to load the other models in runtime
    transactions: List["Transaction"] = Relationship(back_populates="user")


class UserRead(UserBase):
    id: int
    created_at: datetime
    # Done so pydantic knows that the transaction can be a list, None, and by default is None or non existent
    transactions: List["TransactionRead"] | None = None

