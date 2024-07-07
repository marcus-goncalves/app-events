from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.users import CreateUser, UpdateUser, ResponseUser
from services import database
from services import users as user_service

DEFAULT_RESPONSE = {"msg": "to be implemented"}

users = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@users.post(
        path="/",
        status_code=201,
        summary="Creates an user",
        response_model=ResponseUser)
def create_user(user: CreateUser, db: Session = Depends(database.get_session)):
    user_in_db = user_service.get_user_by_email(user.email, db)
    if user_in_db:
        raise HTTPException(
            status_code=400,
            detail=f"{user.email} already registered"
        )
    
    new_user = user_service.create_user(user, db)
    return new_user

@users.patch(
        path="/{user_id}", 
        status_code=202,
        summary="Update user data",
        response_model=ResponseUser)
def update_user(user_id: int, user_data: UpdateUser, db: Session = Depends(database.get_session)):
    user_in_db = user_service.get_user_by_id(user_id, db)
    if not user_in_db:
        raise HTTPException(
            status_code=404,
            detail=f"User {user_id} not found in database"
        )
    
    updated_user = user_service.update_user(user_id, user_data, db)
    return updated_user

@users.delete(
        path="/{user_id}", 
        status_code=200,
        summary="Deletes an user")
def delete_user(user_id: int, db: Session = Depends(database.get_session)):
    user_in_db = user_service.get_user_by_id(user_id, db)
    if not user_in_db:
        raise HTTPException(
            status_code=404,
            detail=f"User {user_id} not found in database"
        )

    old_user = user_service.delete_user(user_id, db)
    return old_user

@users.get(
        path="/", 
        status_code=200,
        summary="Return all users")
def get_all_users(db: Session = Depends(database.get_session)):
    return user_service.get_users(db)

@users.get(
        path="/{email}", 
        status_code=200,
        summary="Return an user by email")
def get_user_by_email(email: str, db: Session = Depends(database.get_session)):
    user_in_db = user_service.get_user_by_email(email, db)
    if not user_in_db:
        raise HTTPException(
            status_code=404,
            detail=f"User {email} not found in database"
        )
    
    return user_in_db