from app.models import Item
from tortoise.exceptions import DoesNotExist, IntegrityError

async def create_item(name: str, description: str) -> Item|None:
    """
    Create a new item in the database with the given name and description.

    Args:
        name (str): The name of the item.
        description (str): The description of the item.

    Returns:
        Item: The created item object.
    
    Raises:
        IntegrityError: If there is a database integrity issue, such as a duplicate entry.
    """
    try:
        item = await Item.create(name=name, description=description)
        return item
    except IntegrityError as e:
        raise IntegrityError("Database integrity error: " + str(e))

async def get_items():
    """
    Retrieve all items from the database.

    Returns:
        list[Item]: A list of all items stored in the database.
    """
    return await Item.all()

async def get_item_by_id(item_id: int) -> Item|None:
    """
    Fetch an item by its id.

    Args:
        item_id (int): The id of the item to retrieve.

    Returns:
        Item or None: The item if found, otherwise None.
    
    Raises:
        DoesNotExist: If the item with the specified ID is not found.
    """
    try:
        return await Item.get(id=item_id)
    except DoesNotExist:
        return None

async def update_item(item_id: int, name: str, description: str) -> Item|None:
    """
    Update an existing item by its id with the new name and description.

    Args:
        item_id (int): The id of the item to update.
        name (str): The new name of the item.
        description (str): The new description of the item.

    Returns:
        Item or None: The updated item if successful, otherwise None.
    
    Raises:
        IntegrityError: If there is a database integrity issue.
    """
    item = await get_item_by_id(item_id)
    if item:
        item.name = name
        item.description = description
        await item.save()
        return item
    return None

async def delete_item(item_id: int) -> Item|None:
    """
    Delete an item by its id.

    Args:
        item_id (int): The id of the item to delete.

    Returns:
        dict: A message indicating success or failure.
    """
    item = await get_item_by_id(item_id)
    if item:
        await item.delete()
        return item
    return None