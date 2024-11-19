from dotenv import load_dotenv
import os
from typing import Annotated

from fastapi import Depends
from sqlmodel import create_engine, Session


# done for loading the local .evn file with the SQL_DATABASE_URL
load_dotenv()

sql_url = os.getenv('SQL_DATABASE_URL')


engine = create_engine(sql_url)


def get_session() -> Session:
    """Creates a unique session each time"""
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
