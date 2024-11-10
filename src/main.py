from fastapi import FastAPI 
from routes import base, data
from motor.motor_asyncio import AsyncIOMotorClient
from helper.config import get_settings


app = FastAPI()


app.include_router(base.base_router)
app.include_router(data.data_router)


@app.on_event("startup")
async def connect_to_db():
    settings = get_settings()
    app.mongodb_connection = AsyncIOMotorClient(settings.MONGODB_URL)
    app.db_client = app.mongodb_connection[settings.MONGODB_DATABASE]

@app.on_event("shutdown")
async def shutdown():
    app.mongodb_connection.close()

