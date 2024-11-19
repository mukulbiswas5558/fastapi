from fastapi import FastAPI
from .routers import products


app = FastAPI()

# Include the user router
app.include_router(products.router)
