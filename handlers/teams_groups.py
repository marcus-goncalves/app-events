from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services import database
from schemas.teams_groups import ResponseTeamsGroup, CreateTeamsGroup, TeamsGroup
from services import teams_groups as teams_group_service
from handlers.utils import convert_key

teams_groups = APIRouter(
    prefix="/teams-group",
    tags=["Teams Group"]
)

@teams_groups.post(
    path="/",
    status_code=201,
    summary="Creates an teams group",
    response_model=ResponseTeamsGroup)
def create_teams_group(teams_group: TeamsGroup, db: Session = Depends(database.get_session)):
    input_tg = CreateTeamsGroup(**teams_group.model_dump(), name_key=convert_key(teams_group.group_name))
    tg_in_db = teams_group_service.get_teams_group_by_key(input_tg.name_key, db)
    if tg_in_db:
        raise HTTPException(
            status_code=400,
            detail=f"{teams_group.group_name} already exists - id: {tg_in_db.id}"
        )
    
    new_tg = teams_group_service.create_teams_group(input_tg, db)
    return new_tg

@teams_groups.delete(
        path="/",
        status_code=200,
        summary="Deletes an teams group")
def delete_teams_group(teams_group_id: int, db: Session = Depends(database.get_session)):
    tg_in_db = teams_group_service.get_teams_group_by_id(teams_group_id, db)
    if not tg_in_db:
        raise HTTPException(
            status_code=404,
            detail=f"id: {teams_group_id} not found"
        )
    
    teams_group_service.delete_teams_group(teams_group_id, db)
    return {}

@teams_groups.get(
        path="/",
        status_code=200,
        summary="Return all teams groups")
def get_all_teams_groups(db: Session = Depends(database.get_session)):
    return teams_group_service.get_all_teams_groups(db)

