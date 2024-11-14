from typing import Annotated

from fastapi import FastAPI, Depends
from sqlmodel import Session

from database import get_session


app = FastAPI()
SessionDep = Annotated[Session, Depends(get_session)]


@app.get("/")
async def root(session: SessionDep):
    return {"message": "Hello World"}