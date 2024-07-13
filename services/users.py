from sqlalchemy.orm import Session
from schemas import users
from db_models import users as users_db

def create_user(user: users.CreateUser, db: Session):
    db_user = users_db.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(user_id: int, user_data: users.UpdateUser, db: Session):
    db_user = db.query(users_db.User).filter(users_db.User.id == user_id)
    new_user = db_user.first()

    db_user.update(
        user_data.model_dump(exclude_none=True),
        synchronize_session=False)
    
    db.commit()
    db.refresh(new_user)
    return new_user

def delete_user(user_id: int, db: Session):
    db_user = db.query(users_db.User).filter(users_db.User.id == user_id)
    db_user.delete(synchronize_session=False)
    db.commit()
    return 

def get_user_by_email(email: str, db: Session):
    return db.query(users_db.User).filter(users_db.User.email == email).first()

def get_user_by_id(user_id: int, db: Session):
    return db.query(users_db.User).filter(users_db.User.id == user_id).first()

def get_users(db: Session):
    res = db.query(users_db.User).all()
    return res