from fastapi import FastAPI, status, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from app.router import item
from app.db import lifespan

app = FastAPI(lifespan=lifespan)
app.include_router(item.router)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    '''
    Function to handle exception from fastapi when get invalid input
    '''
    # Create a custom response that returns a 400 Bad Request
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={'detail': 'Invalid input data', 'errors': exc.errors()},
    )

@app.get('/')
async def root():
    return {'message': 'Hello World'}
