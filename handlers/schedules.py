from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services import database
from schemas.schedules import ResponseSchedule, CreateSchedule, Schedule
from services import schedules as schedule_service
from handlers.utils import convert_key

schedules = APIRouter(
    prefix="/schedules",
    tags=["Schedules"]
)

@schedules.post(
    path="/",
    status_code=201,
    summary="Creates a schedule",
    response_model=ResponseSchedule)
def create_schedule(schedule: Schedule, db: Session = Depends(database.get_session)):
    input_sched = CreateSchedule(**schedule.model_dump(), name_key=convert_key(schedule.description))
    sched_in_db = schedule_service.get_schedule_by_key(input_sched.name_key, db)
    if sched_in_db:
        raise HTTPException(
            status_code=400,
            detail=f"{schedule.description} already exists - id: {sched_in_db.id}"
        )
    
    new_sched = schedule_service.create_schedule(input_sched, db)
    return new_sched

@schedules.delete(
        path="/",
        status_code=200,
        summary="Deletes a schedule")
def delete_schedule(schedule_id: int, db: Session = Depends(database.get_session)):
    sched_in_db = schedule_service.get_schedule_by_id(schedule_id, db)
    if not sched_in_db:
        raise HTTPException(
            status_code=404,
            detail=f"id: {schedule_id} not found"
        )
    
    schedule_service.delete_schedule(schedule_id, db)
    return {}

@schedules.get(
        path="/",
        status_code=200,
        summary="Return al schedules")
def get_all_schedules(db: Session = Depends(database.get_session)):
    return schedule_service.get_all_schedules(db)

