from fastapi import APIRouter, HTTPException
from ..services.user_client import get_user_data
from ..services.product_client import get_product_data

router = APIRouter()

@router.get("/users/{user_id}")
async def get_user(user_id: int):
    user = await get_user_data(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/products/{product_id}")
async def get_post(product_id: int):
    post = await get_product_data(product_id)
    if not post:
        raise HTTPException(status_code=404, detail="Product not found")
    return post


