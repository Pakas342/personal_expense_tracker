from typing import Annotated

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.database import get_session
from app.models import TransactionRead, Transaction, TransactionBase

transaction_router = APIRouter(
    prefix='/user/transaction'
)

SessionDep = Annotated[Session, Depends(get_session)]


@transaction_router.get("/", response_model=list[TransactionRead])
def get_transactions(
        user_id: int,
        db: SessionDep,
        skip: int = 0,
        limit: int = 100
) -> list[TransactionRead]:
    statement = select(Transaction).where(Transaction.user_id == user_id).offset(skip).limit(limit)
    result = db.exec(statement=statement).all()
    return [TransactionRead.model_validate(transaction.model_dump()) for transaction in result]


@transaction_router.get('/{id}')
def get_transaction(user_id: int, transaction_id: int, db: SessionDep) -> TransactionRead:
    statement = select(Transaction).where(Transaction.id == transaction_id).where(Transaction.user_id == user_id)
    transaction = db.exec(statement).first()
    return TransactionRead.model_validate(transaction.model_dump())


# Sin revisar porque necesitamos un user primero
@transaction_router.post('/')
def create_transaction(user_id: int, transaction: TransactionBase, db: SessionDep):
    new_transaction = Transaction.model_validate(transaction)
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return TransactionRead.model_validate(new_transaction.model_dump())
