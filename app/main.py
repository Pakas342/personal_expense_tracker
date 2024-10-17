from fastapi import FastAPI, Depends
from sqlmodel import Session
from typing import Annotated

from database import get_session
from models import TransactionRead, Transaction


app = FastAPI()
SessionDep = Annotated[Session, Depends(get_session)]


@app.get("/")
async def root(session: SessionDep):
    return {"message": "Hello World"}
