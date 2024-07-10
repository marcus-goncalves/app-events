from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services import database
from schemas.work_shifts import ResponseWorkShift, CreateWorkShift, WorkShift
from services import work_shifts as work_shift_service
from handlers.utils import convert_key

work_shifts = APIRouter(
    prefix="/work-shifts",
    tags=["Work Shifts"]
)

@work_shifts.post(
    path="/",
    status_code=201,
    summary="Creates an work shift",
    response_model=ResponseWorkShift)
def create_work_shift(work_shift: WorkShift, db: Session = Depends(database.get_session)):
    input_ws = CreateWorkShift(**work_shift.model_dump(), name_key=convert_key(work_shift.description))
    ws_in_db = work_shift_service.get_work_shift_by_key(input_ws.name_key, db)
    if ws_in_db:
        raise HTTPException(
            status_code=400,
            detail=f"{work_shift.description} already exists - id: {ws_in_db.id}"
        )
    
    new_ws = work_shift_service.create_work_shift(input_ws, db)
    return new_ws

@work_shifts.delete(
        path="/",
        status_code=200,
        summary="Deletes an work shift")
def delete_work_shift(work_shift_id: int, db: Session = Depends(database.get_session)):
    ws_in_db = work_shift_service.get_work_shift_by_id(work_shift_id, db)
    if not ws_in_db:
        raise HTTPException(
            status_code=404,
            detail=f"id: {work_shift_id} not found"
        )
    
    work_shift_service.delete_work_shift(work_shift_id, db)
    return {}

@work_shifts.get(
        path="/",
        status_code=200,
        summary="Return all work shifts")
def get_all_work_shifts(db: Session = Depends(database.get_session)):
    return work_shift_service.get_all_work_shifts(db)

