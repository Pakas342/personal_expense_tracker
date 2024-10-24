from fastapi import APIRouter, Depends, Query
from typing import Annotated
from sqlmodel import Session, select

from ..models import TransactionRead, Transaction
from ..database import get_session

transaction_router = APIRouter(
    prefix='/transaction'
)

SessionDep = Annotated[Session, Depends(get_session)]


@transaction_router.get("/", response_model=list[TransactionRead])
def get_transactions(
        db=SessionDep,
        skip: int = 0,
        limit: int = 100
) -> list[TransactionRead]:
    statement = select(Transaction).offset(skip).limit(limit)
    result = db.exec(statement=statement).all()
    return [TransactionRead.model_validate(transaction.model_dump()) for transaction in result]


@transaction_router.get('/{id}')
async def get_transaction(transaction_id: int, db=SessionDep) -> TransactionRead:
    statement = select(Transaction).where(Transaction.id == transaction_id)
    transaction = db.exec(statement)
    return TransactionRead.model_validate(transaction.model_dump())
