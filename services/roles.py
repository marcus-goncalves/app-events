from sqlalchemy.orm import Session
from schemas import roles
from db_models import roles as roles_db


def create_role(role: roles.CreateRole, db: Session):
    db_role = roles_db.Role(**role.model_dump())
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def delete_role(role_id: int, db: Session):
    db_role = db.query(roles_db.Role).filter(roles_db.Role.id == role_id)
    db_role.delete(synchronize_session=False)
    db.commit()
    return

def get_all_roles(db: Session):
    roles: list = db.query(roles_db.Role).all()
    return {"data": roles}

def get_role_by_name(role_name: str, db: Session):
    return db.query(roles_db.Role).filter(roles_db.Role.name == role_name).first()

def get_role_by_id(role_id: int, db: Session):
    return db.query(roles_db.Role).filter(roles_db.Role.id == role_id).first()