import httpx

async def get_item_data(item_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://item_service:8003/items/{item_id}")
        if response.status_code == 200:
            return response.json()
        return None
