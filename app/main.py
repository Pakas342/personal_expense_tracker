from fastapi import FastAPI, Depends

from app.router import transaction_router

app = FastAPI()
app.include_router(transaction_router)
