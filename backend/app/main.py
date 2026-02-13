import uvicorn
from fastapi import FastAPI
from app.api.v1 import expenses, income

app = FastAPI(
    title="Personal Finance tracker",
    description="API that will handle new and update existing transactions for the personal finane API.",
    version="1.0.0"
)

app.include_router(income.router)
app.include_router(expenses.router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)