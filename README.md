# FastAPI async CRUD
This project provides an asynchronous **CRUD (Create, Read, Update, Delete)** API for managing items on database using **FastAPI**. It uses **SQLite** for data storage and **Tortoise ORM** to handle ORM with database to build a RESTful API with asynchronous database operations.

## Project Description
This application allows users to perform basic CRUD operations on Item model with attributes `id`, `name` and `description`. It uses **Tortoise ORM** for asynchronous database interaction and **Pydantic models** for input validation. The app includes endpoints for:

- **Creating** a new item
- **Reading** all items or a specific item by its ID
- **Updating** an item by ID
- **Deleting** an item by ID

## Setup Instruction

### Local environment

#### 1. Clone the repository
``` bash
git clone https://github.com/unikrubii/fastapi-async-crud.git
cd fastapi-async-crud
```

#### 2. Create and activate a virtual environment
``` bash
python3 -m venv .venv
source .venv/bin/activate
```

#### 3. Install the required dependencies
``` bash
pip install -r requirements.txt
```

### 4. Run the application
start FastAPI server with the following command
``` bash
fastapi dev app/main.py
```

This will start the server at http://127.0.0.1:8000. You can test the API endpoints by navigating to:
- `POST /items/` - Create a new item
- `GET /items/` - Get all items
- `GET /items/{item_id}/` - Get a specific item by ID
- `PUT /items/{item_id}/` - Update an item by ID
- `DELETE /items/{item_id}/` - Delete an item by ID

The FastAPI documentation is available at http://127.0.0.1:8000/docs.


## API Usage examples
### 1. Create an item (Post `/items/`)
Request
``` bash
curl -X 'POST' \
  'http://127.0.0.1:8000/items/' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Test Item",
  "description": "This is a test item."
}'
```
Response
``` bash
{ "id": 1 }
```

### 2. Get all items (GET `/items/`)
Request
``` bash
curl -X 'GET' 'http://127.0.0.1:8000/items/'
```
Response
``` bash
[
  {
    "id": 1,
    "name": "Test Item",
    "description": "This is a test item."
  }
]
```

### 3. Get item by id (Get `/items/{item_id}`)
Request
``` bash
curl -X 'GET' 'http://127.0.0.1:8000/items/1/'
```
Response
``` bash
{
  "id": 1,
  "name": "Test Item",
  "description": "This is a test item."
}
```

### 4. Update an item (PUT `/items/{item_id}`)
Request
``` bash
curl -X 'PUT' \
  'http://127.0.0.1:8000/items/1/' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Updated Test Item",
  "description": "Updated description."
}'
```
Response
``` bash
{
  "id": 1,
  "name": "Updated Test Item",
  "description": "Updated description."
}
```

### 5. Delete an item (DELETE `/items/{item_id}`)
Request
``` bash
curl -X 'DELETE' 'http://127.0.0.1:8000/items/1/'
```
Response
``` bash
{ "message": "Item with id 1 deleted successfully" }
```

## Testing Instruction
### Running test
To run all tests, use the following command:
``` bash
pytest
```
You can add the `-v` flag to get more verbose output:
``` bash
pytest -v
```

To run a test in a module
``` bash
pytest app/tests/test_crud.py
```

To run a test by Node IDS with syntax `filename.py::test_function_name`
``` bash
pytest app/tests/test_crud.py::test_create_item
```