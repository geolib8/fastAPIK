from fastapi import APIRouter, HTTPException, status
from models.todos import Todo
from schema.schemas import list_serial, individual_serial
from config.db import collection_name
from bson import ObjectId

router = APIRouter()

# GET all todos
@router.get("/", status_code=status.HTTP_200_OK, response_description="List all todos")
async def get_todos():
    todos = list_serial(collection_name.find())
    return {"data": todos}

# GET a single todo
@router.get("/{id}", status_code=status.HTTP_200_OK, response_description="Get a todo by ID")
async def get_todo(id: str):
    todo = collection_name.find_one({"_id": ObjectId(id)})
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"data": individual_serial(todo)}

# POST a new todo
@router.post("/", status_code=status.HTTP_201_CREATED, response_description="Create a new todo")
async def post_todo(todo: Todo):
    result = collection_name.insert_one(dict(todo))
    new_todo = collection_name.find_one({"_id": result.inserted_id})
    return {"message": "Todo created successfully", "data": individual_serial(new_todo)}

# PUT (update) a todo
@router.put("/{id}", status_code=status.HTTP_200_OK, response_description="Update a todo")
async def put_todo(id: str, todo: Todo):
    updated_todo = collection_name.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": dict(todo)},
        return_document=True
    )
    if not updated_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo updated successfully", "data": individual_serial(updated_todo)}

# DELETE a todo
@router.delete("/{id}", status_code=status.HTTP_200_OK, response_description="Delete a todo")
async def delete_todo(id: str):
    deleted_todo = collection_name.find_one_and_delete({"_id": ObjectId(id)})
    if not deleted_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully", "data": individual_serial(deleted_todo)}
