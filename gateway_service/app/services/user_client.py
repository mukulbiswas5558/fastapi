import httpx

async def get_user_data(user_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://user_service:8001/users/{user_id}")
        if response.status_code == 200:
            return response.json()
        return None
