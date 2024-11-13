import httpx

async def get_post_data(post_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://post_service:8002/posts/{post_id}")
        if response.status_code == 200:
            return response.json()
        return None
