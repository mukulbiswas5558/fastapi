from fastapi import APIRouter, HTTPException
from ..models import User

router = APIRouter()

fake_users_db = {
    1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
    2: {"id": 2, "name": "Bob", "email": "bob@example.com"}
}

@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    user = fake_users_db.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
