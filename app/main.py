from fastapi import FastAPI
from router import transaction_router

app = FastAPI()
app.include_router(transaction_router)
