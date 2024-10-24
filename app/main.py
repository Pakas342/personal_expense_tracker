from fastapi import FastAPI
from app.router import transaction_router

app = FastAPI()
app.include_router(transaction_router)
