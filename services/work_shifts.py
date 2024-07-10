from sqlalchemy.orm import Session
from schemas import work_shifts
from db_models import work_shifts as work_shifts_db

def create_work_shift(work_shift: work_shifts.WorkShift, db: Session):
    db_work_shift = work_shifts_db.WorkShift(**work_shift.model_dump())
    db.add(db_work_shift)
    db.commit()
    db.refresh(db_work_shift)
    return db_work_shift

def delete_work_shift(work_shift_id: int, db: Session):
    db_work_shift = db.query(work_shifts_db.WorkShift).filter(work_shifts_db.WorkShift.id == work_shift_id)
    db_work_shift.delete(synchronize_session=False)
    db.commit()
    return

def get_all_work_shifts(db: Session):
    work_shifts = db.query(work_shifts_db.WorkShift).all()
    return {"data": work_shifts}

def get_work_shift_by_key(work_shift_key: str, db: Session):
    return db.query(work_shifts_db.WorkShift).filter(work_shifts_db.WorkShift.name_key == work_shift_key).first()

def get_work_shift_by_id(work_shift_id: int, db: Session):
    return db.query(work_shifts_db.WorkShift).filter(work_shifts_db.WorkShift.id == work_shift_id).first()