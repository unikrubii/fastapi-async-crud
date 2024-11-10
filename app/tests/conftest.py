import pytest
from app.main import app
from fastapi.testclient import TestClient
from tortoise import Tortoise

@pytest.fixture
async def init_db():
    '''
    Initializes the database for testing, including the creation of schemas.
    '''
    # Initialize the in-memory database (SQLite)
    await Tortoise.init(
        db_url='sqlite://:memory:',
        modules={'models': ['app.models']}
    )
    # Generate schemas for the models
    await Tortoise.generate_schemas()

    # Yield the execution back to the test
    yield

    # Clean up database connections after test
    await Tortoise.close_connections()

@pytest.fixture
def client(init_db):
    '''
    Creates and provides a TestClient instance for making API calls.
    '''
    return TestClient(app)
