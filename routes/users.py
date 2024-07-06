from fastapi import APIRouter
from models.users import CreateUser, UpdateUser

DEFAULT_RESPONSE = {"msg": "to be implemented"}

users = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@users.post(
        path="/",
        status_code=201,
        summary="Creates an user",)
def create_user(user: CreateUser):
    return DEFAULT_RESPONSE

@users.patch(
        path="/{user_id}", 
        status_code=202,
        summary="Update user data")
def update_user(user_id: int, user_data: UpdateUser):
    return DEFAULT_RESPONSE

@users.delete(
        path="/{user_id}", 
        status_code=200,
        summary="Deletes an user")
def delete_user(user_id: int):
    return DEFAULT_RESPONSE

@users.get(
        path="/", 
        status_code=200,
        summary="Return all users")
def get_all_users():
    return DEFAULT_RESPONSE

@users.get(
        path="/{email}", 
        status_code=200,
        summary="Return an user by email")
def get_user_by_email(email: str):
    return DEFAULT_RESPONSE