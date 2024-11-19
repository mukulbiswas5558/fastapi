from dotenv import load_dotenv
import os
import httpx

load_dotenv()

# Get the POST_SERVICE_URL from environment variables
PRODUCT_SERVICE_URL = os.getenv("PRODUCT_SERVICE_URL")
    
async def get_product_data(product_id: int):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{PRODUCT_SERVICE_URL}/products/{product_id}")
            if response.status_code == 200:
                return response.json()
            return None
    except httpx.RequestError as e:
        print(f"Request error: {e}")
        return None