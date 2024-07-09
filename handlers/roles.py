from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services import database
from schemas.roles import ResponseRole, CreateRole
from services import roles as role_service


roles = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)

@roles.post(
    path="/",
    status_code=201,
    summary="Creates a role",
    response_model=ResponseRole)
def create_role(role: CreateRole, db: Session = Depends(database.get_session)):
    role_in_db = role_service.get_role_by_name(role.name, db)
    if role_in_db:
        raise HTTPException(
            status_code=400,
            detail=f"{role.name} already exists - id: {role_in_db.id}"
        )

    new_role = role_service.create_role(role, db)
    return new_role


@roles.delete(
    path="/",
    status_code=200,
    summary="Deletes a role")
def delete_role(role_id: int, db: Session = Depends(database.get_session)):
    role_in_db = role_service.get_role_by_id(role_id, db)
    if not role_in_db:
        raise HTTPException(
            status_code=404,
            detail=f"id {role_id} not found"
        )
    
    role_service.delete_role(role_id, db)
    return {}


@roles.get(
    path="/",
    status_code=200,
    summary="Return all roles")
def get_all_roles(db: Session = Depends(database.get_session)):
    return role_service.get_all_roles(db)