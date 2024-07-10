from sqlalchemy.orm import Session
from schemas import schedules
from db_models import schedules as schedules_db

def create_schedule(schedule: schedules.Schedule, db: Session):
    db_schedule = schedules_db.Schedule(**schedule.model_dump())
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule

def delete_schedule(schedule_id: int, db: Session):
    db_schedule = db.query(schedules_db.Schedule).filter(schedules_db.Schedule.id == schedule_id)
    db_schedule.delete(synchronize_session=False)
    db.commit()
    return

def get_all_schedules(db: Session):
    schedules = db.query(schedules_db.Schedule).all()
    return {"data": schedules}

def get_schedule_by_key(schedule_key: str, db: Session):
    return db.query(schedules_db.Schedule).filter(schedules_db.Schedule.name_key == schedule_key).first()

def get_schedule_by_id(schedule_id: int, db: Session):
    return db.query(schedules_db.Schedule).filter(schedules_db.Schedule.id == schedule_id).first()