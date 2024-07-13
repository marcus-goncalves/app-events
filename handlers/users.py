from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.users import CreateUser, UpdateUser, ResponseUser
from services import database
from services import users as user_service
from services import roles as role_service
from services import schedules as schedule_service
from services import work_shifts as work_shift_service
from services import teams_groups as teams_group_service

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
    
    _check_role(user.id_role, db)
    _check_schedule(user.id_schedule, db)
    _check_work_shift(user.id_work_shift, db)
    _check_teams_group(user.id_teams_group, db)

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
    
    if user_data.id_role:
        _check_role(user_data.id_role, db)
        
    if user_data.id_schedule:
        _check_schedule(user_data.id_schedule, db)
    
    if user_data.id_schedule:
        _check_work_shift(user_data.id_work_shift, db)

    if user_data.id_teams_group:
        _check_teams_group(user_data.id_teams_group, db)

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
        summary="Return all users",
        response_model=list[ResponseUser])
def get_all_users(db: Session = Depends(database.get_session)):
    return user_service.get_users(db)

@users.get(
        path="/{email}", 
        status_code=200,
        summary="Return an user by email",
        response_model=ResponseUser)
def get_user_by_email(email: str, db: Session = Depends(database.get_session)):
    user_in_db = user_service.get_user_by_email(email, db)
    if not user_in_db:
        raise HTTPException(
            status_code=404,
            detail=f"User {email} not found in database"
        )
    
    return user_in_db


def _check_role(id_role, db):
    check_role_id = role_service.get_role_by_id(id_role, db)
    if not check_role_id or check_role_id.is_active == False:
        raise HTTPException(
            status_code=400,
            detail=f"please inform a valid role. Id: {id_role} is invalid"
        )
    return

def _check_schedule(id_schedule, db):
    check_schedule_id = schedule_service.get_schedule_by_id(id_schedule, db)
    if not check_schedule_id:
        raise HTTPException(
            status_code=400,
            detail=f"please inform a valid schedule. Id: {id_schedule} is invalid"
        )
    return

def _check_work_shift(id_work_shift, db):
    ws_id = work_shift_service.get_work_shift_by_id(id_work_shift, db)
    if not ws_id:
        raise HTTPException(
            status_code=400,
            detail=f"please inform a valid work shift. Id: {id_work_shift} is invalid"
        )
    return

def _check_teams_group(id_teams_group, db):
    tg_id = teams_group_service.get_teams_group_by_id(id_teams_group, db)
    if not tg_id:
        raise HTTPException(
            status_code=400,
            detail=f"please inform a valid teams group. Id: {id_teams_group} is invalid"
        )
    return