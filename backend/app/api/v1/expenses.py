from fastapi import APIRouter

router = APIRouter()

@router.post("/get")
async def list_expenses():
    pass