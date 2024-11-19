from fastapi import APIRouter, Depends

from app.database import SessionDep
from app.models import User, UserRead, UserBase

user_router = APIRouter(
    prefix='/auth'
)


@user_router.post(path='/signup', response_model=UserRead)
def user_signup(user: UserBase, db: SessionDep) -> UserRead:
    new_user = User.model_validate(user)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return UserRead.model_validate(new_user.model_dump())
