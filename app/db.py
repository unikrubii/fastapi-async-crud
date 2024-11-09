from tortoise import Tortoise
from fastapi import FastAPI
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    A lifespan context manager to initialize and close the database connection.
    This will be used to ensure the database is ready when the app starts and closed when the app shuts down.
    """
    # Initialize the database connection
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",
        modules={"models": ["app.models"]}
    )
    await Tortoise.generate_schemas()
    yield
    await Tortoise.close_connections()
