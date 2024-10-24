from fastapi import APIRouter, Depends
from typing import Annotated
from sqlmodel import Session

from ..models import TransactionRead
from ..database import get_session

transaction_router = APIRouter(
    prefix='/transaction'
)

SessionDep = Annotated[Session, Depends(get_session)]


@transaction_router.get("/")
async def get_transactions(db=SessionDep) -> list[TransactionRead]:
    pass


@transaction_router.get('/{id}')
async def get_transaction(id: int) -> TransactionRead:
    pass
