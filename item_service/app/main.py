from fastapi import FastAPI
from .routers import items
from .database import initialize_db

app = FastAPI()

# Include the item router
app.include_router(items.router)

@app.on_event("startup")
def startup_event():
    initialize_db()
