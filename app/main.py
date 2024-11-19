from fastapi import FastAPI

from app.router import transaction_router, user_router

app = FastAPI()
app.include_router(transaction_router)
app.include_router(user_router)
