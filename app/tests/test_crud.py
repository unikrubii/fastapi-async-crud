import pytest
from app.crud import create_item, get_items, get_item_by_id, update_item, delete_item
from app.models import Item
from app.tests.conftest import init_db


import pytest
from fastapi.testclient import TestClient
from tortoise import Tortoise
from app.main import app
from app.models import Item

# @pytest.mark.asyncio
# async def test_create_item(client):
#     '''
#     Tests the FastAPI endpoint that creates an item in the database.
#     '''
#     # Data to create a new item
#     data = {'name': 'Test Item', 'description': 'This is a test item'}

#     # Make a POST request to the FastAPI endpoint
#     response = client.post('/items', json=data)

#     # Check that the response status code is 201 (Created)
#     assert response.status_code == 201

#     # Verify that the item is in the database by querying for it
#     item = await Item.get(name='Test Item')
#     assert item is not None
#     assert item.name == 'Test Item'
#     assert item.description == 'This is a test item'


@pytest.mark.asyncio
async def test_create_item(init_db):
    '''
    Tests the create_item function from the CRUD module.
    '''
    # Create a new item using the function
    item = await create_item(name='Test Item', description='Test Description')

    # Assert the item was created successfully and matches the input
    assert item is not None
    assert item.name == 'Test Item'
    assert item.description == 'Test Description'

@pytest.mark.asyncio
async def test_get_items(init_db):
    '''
    Tests the get_items function from the CRUD module.
    '''
    # Create some items
    await create_item(name='Item 1', description='First item')
    await create_item(name='Item 2', description='Second item')

    # Call get_items to retrieve all items
    items = await get_items()

    # Assert that we got two items
    assert len(items) == 2
    assert all(isinstance(item, Item) for item in items)


@pytest.mark.asyncio
async def test_get_item_by_id(init_db):
    '''
    Tests the get_item_by_id function from the CRUD module.
    '''
    # Create an item
    item = await create_item(name='Item 1', description='Description for item 1')

    # Fetch the item by ID using the function
    fetched_item = await get_item_by_id(item.id)

    # Assert that the fetched item is correct
    assert fetched_item is not None
    assert fetched_item.id == item.id
    assert fetched_item.name == 'Item 1'
    assert fetched_item.description == 'Description for item 1'


@pytest.mark.asyncio
async def test_get_item_by_id_not_found(init_db):
    '''
    Tests that get_item_by_id returns None when the item is not found.
    '''
    # Try to fetch an item that doesn't exist
    fetched_item = await get_item_by_id(999)  # Using a random ID that doesn't exist

    # Assert that None is returned since the item does not exist
    assert fetched_item is None


@pytest.mark.asyncio
async def test_update_item(init_db):
    '''
    Tests the update_item function from the CRUD module.
    '''
    # Create an item to update
    item = await create_item(name='Item 1', description='Old Description')

    # Update the item
    updated_item = await update_item(item.id, name='Updated Item', description='Updated Description')

    # Assert that the item was updated
    assert updated_item is not None
    assert updated_item.name == 'Updated Item'
    assert updated_item.description == 'Updated Description'


@pytest.mark.asyncio
async def test_update_item_not_found(init_db):
    '''
    Tests that update_item returns None when the item is not found.
    '''
    # Try to update an item that doesn't exist
    updated_item = await update_item(999, name='Non-existent Item', description='Non-existent Description')

    # Assert that None is returned since the item doesn't exist
    assert updated_item is None


@pytest.mark.asyncio
async def test_delete_item(init_db):
    '''
    Tests the delete_item function from the CRUD module.
    '''
    # Create an item to delete
    item = await create_item(name='Item to Delete', description='Item description')

    # Delete the item
    deleted_item = await delete_item(item.id)

    # Assert that the item was deleted
    assert deleted_item is not None
    assert deleted_item.id == item.id


@pytest.mark.asyncio
async def test_delete_item_not_found(init_db):
    '''
    Tests that delete_item returns None when the item is not found.
    '''
    # Try to delete an item that doesn't exist
    deleted_item = await delete_item(999)  # Using a random ID that doesn't exist

    # Assert that None is returned since the item doesn't exist
    assert deleted_item is None
