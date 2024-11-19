from datetime import timedelta, datetime

from pydantic import BaseModel
import jwt
from passlib.context import CryptContext
from sqlmodel import select

from app.database import SessionDep
from app.models import User

SECRET_KEY = 'd4719ef68dfc0f0a6f825b898772540dd27cd9e414550b90f05ce4176f89ff57'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 1440

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Token(BaseModel):
    access_token: str
    token_type: str


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(hashed_password: str, plain_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_user(db: SessionDep, email: str) -> User | bool:
    statement = select(User).where(User.email == email)
    user = db.exec(statement=statement).first()
    if not user:
        return False
    else:
        return user


def authenticate_user(db: SessionDep, email: str, password: str) -> User | bool:
    user = get_user(db=db, email=email)
    if not user:
        return False
    if not verify_password(user.password, password):
        return False
    return user


def create_access_token(data_to_encode: dict, expire_delta: timedelta | None = None) -> jwt:
    to_encode = data_to_encode.copy()
    if expire_delta:
        expire = datetime.now() + expire_delta
    else:
        expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})
    return jwt.encode(payload=to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
