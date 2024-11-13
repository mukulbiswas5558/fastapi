from fastapi import FastAPI
from .routers import users
from .database import initialize_db

app = FastAPI()

# Include the user router
app.include_router(users.router)

@app.on_event("startup")
def startup_event():
    initialize_db()
