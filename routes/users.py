from fastapi import APIRouter

DEFAULT_RESPONSE = {"msg": "to be implemented"}

users = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@users.post(path="/",status_code=201)
def create_user():
    return DEFAULT_RESPONSE

@users.patch(path="/{user_id}", status_code=202)
def update_user(user_id: int):
    return DEFAULT_RESPONSE

@users.delete(path="/{user_id}", status_code=200)
def delete_user(user_id: int):
    return DEFAULT_RESPONSE

@users.get(path="/", status_code=200)
def get_all_users():
    return DEFAULT_RESPONSE

@users.get(path="/{email}", status_code=200)
def get_user_by_email(email: str):
    return DEFAULT_RESPONSE