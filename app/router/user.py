from typing import Annotated

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.database import get_session
from app.models import User, UserRead, UserBase

user_router = APIRouter(
    prefix='/auth'
)
SessionDep = Annotated[Session, Depends(get_session)]


@user_router.post(path='/signup', response_model=UserRead)
def user_signup(user: UserBase, db: SessionDep) -> UserRead:
    new_user = User.model_validate(user)
    db.add(new_user)
    db.commit()
    return UserRead.model_validate(new_user.model_dump())
