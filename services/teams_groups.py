from sqlalchemy.orm import Session
from schemas import teams_groups
from db_models import teams_groups as teams_groups_db

def create_teams_group(teams_group: teams_groups.TeamsGroup, db: Session):
    db_teams_group = teams_groups_db.TeamsGroup(**teams_group.model_dump())
    db.add(db_teams_group)
    db.commit()
    db.refresh(db_teams_group)
    return db_teams_group

def delete_teams_group(teams_group_id: int, db: Session):
    db_teams_group = db.query(teams_groups_db.TeamsGroup).filter(teams_groups_db.TeamsGroup.id == teams_group_id)
    db_teams_group.delete(synchronize_session=False)
    db.commit()
    return

def get_all_teams_groups(db: Session):
    teams_groups = db.query(teams_groups_db.TeamsGroup).all()
    return {"data": teams_groups}

def get_teams_group_by_key(teams_group_key: str, db: Session):
    return db.query(teams_groups_db.TeamsGroup).filter(teams_groups_db.TeamsGroup.name_key == teams_group_key).first()

def get_teams_group_by_id(teams_group_id: int, db: Session):
    return db.query(teams_groups_db.TeamsGroup).filter(teams_groups_db.TeamsGroup.id == teams_group_id).first()