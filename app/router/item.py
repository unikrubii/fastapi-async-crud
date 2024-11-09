from fastapi import APIRouter, HTTPException, status
from pydantic import ValidationError

from tortoise.exceptions import OperationalError, DBConnectionError

from app.models import Item_Pydantic, ItemIn_Pydantic, ItemOut_Pydantic
from app.crud import create_item, get_items, get_item_by_id, update_item, delete_item

router = APIRouter(
    prefix='/items',
    tags=['Items']
)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_new_item(item: ItemIn_Pydantic):
    '''
    Create new item in database
    '''
    try:
        item_obj = await create_item(**item.model_dump())
        return await ItemOut_Pydantic.from_tortoise_orm(item_obj)
    except (OperationalError, DBConnectionError) as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f'Internal server error: {str(e)}')
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f'Unexpected error: {str(e)}')

@router.get('/', status_code=status.HTTP_200_OK)
async def retrieve_all_item():
    '''
    Retrieve all items from database
    '''
    item_objs = await get_items()
    return [await Item_Pydantic.from_tortoise_orm(item_obj) for item_obj in item_objs]

@router.get('/{item_id}', status_code=status.HTTP_200_OK)
async def retrieve_item_by_id(item_id: int):
    '''
    Retrieve item from database by id
    '''
    item_obj = await get_item_by_id(item_id)
    if not item_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Item with id {item_id} not found.')
    return await Item_Pydantic.from_tortoise_orm(item_obj)

@router.put('/{item_id}', status_code=status.HTTP_200_OK)
async def update_item_by_id(item_id: int, item: ItemIn_Pydantic):
    '''
    Update item from databse
    '''
    item_obj = await update_item(item_id, **item.model_dump())
    if not item_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Item with id {item_id} not found.')
    return await Item_Pydantic.from_tortoise_orm(item_obj)

@router.delete('/{item_id}', status_code=status.HTTP_200_OK)
async def delete_item_by_id(item_id: int):
    '''
    Remove item from database
    '''
    deleted_item = await delete_item(item_id)
    if not deleted_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'item id {item_id} does not exist')
    return {'message': f'Item with id {item_id} deleted successfully'}
