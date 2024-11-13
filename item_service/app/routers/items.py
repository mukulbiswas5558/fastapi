from fastapi import APIRouter, HTTPException
from ..models import Item

router = APIRouter()

fake_items_db = {
    1: {"id": 1, "name": "Item One", "description": "Description of item one"},
    2: {"id": 2, "name": "Item Two", "description": "Description of item two"}
}

@router.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    item = fake_items_db.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
