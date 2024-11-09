import pytest
from app.main import app
from app.models import Item
from app.tests.conftest import client

@pytest.mark.asyncio
async def test_create_item(client):
    '''
    Tests the endpoint that creates an item in the database.
    '''
    # Data to create a new item
    data = {'name': 'Test Item', 'description': 'This is a test item'}

    # Make a POST request to the endpoint
    response = client.post('/items', json=data)

    # Check the response status code
    assert response.status_code == 201

    # Verify that the item is in the database by querying for it
    item = await Item.get(name='Test Item')
    assert item is not None
    assert item.name == 'Test Item'
    assert item.description == 'This is a test item'

@pytest.mark.asyncio
async def test_get_all_items(client):
    '''
    Test fetching all items from the database.
    '''
    # Make sure there are items in the database before testing
    await Item.create(name='Item 1', description='Description 1')

    response = client.get('/items/')

    # Check that the response is successful and contains items
    assert response.status_code == 200
    assert len(response.json()) > 0

@pytest.mark.asyncio
async def test_get_item_by_id(client):
    '''
    Tests the endpoint that retrieves an item by its id.
    '''
    item = await Item.create(name='Item 2', description='Description 2')
    
    response = client.get(f'/items/{item.id}/')

    # Check the response status and data
    assert response.status_code == 200
    assert response.json()['name'] == 'Item 2'
    assert response.json()['description'] == 'Description 2'


@pytest.mark.asyncio
async def test_get_item_by_id_not_found(client):
    '''
    Tests the endpoint for retrieving a non-existent item.
    '''
    response = client.get('/items/999999/')

    # Check that a 404 is returned
    assert response.status_code == 404
    assert response.json()['detail'] == 'Item with id 999999 not found.'

@pytest.mark.asyncio
async def test_update_item(client):
    '''
    Tests the endpoint for updating an existing item.
    '''
    item = await Item.create(name='Item 3', description='Description 3')

    data = {'name': 'Updated Item', 'description': 'Updated Description'}
    
    # Perform the update
    response = client.put(f'/items/{item.id}/', json=data)

    # Check the response and ensure the item is updated
    assert response.status_code == 200
    assert response.json()['name'] == 'Updated Item'
    assert response.json()['description'] == 'Updated Description'

    # Verify item is updated in the database
    updated_item = await Item.get(id=item.id)
    assert updated_item.name == 'Updated Item'
    assert updated_item.description == 'Updated Description'

@pytest.mark.asyncio
async def test_update_item_not_found(client):
    '''
    Tests the endpoint for updating a non-existent item.
    '''
    data = {'name': 'Non Existent Item', 'description': 'This item does not exist'}

    response = client.put('/items/999999/', json=data)

    # Check that a 404 is returned
    assert response.status_code == 404
    assert response.json()['detail'] == 'Item with id 999999 not found.'

@pytest.mark.asyncio
async def test_delete_item_not_found(client):
    '''
    Tests the endpoint for trying to delete a non-existent item.
    '''
    response = client.delete('/items/999999/')

    # Check that a 404 is returned
    assert response.status_code == 404
    assert response.json()['detail'] == 'item id 999999 does not exist'
