from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter()

@router.post("/create", response_model=schemas.GroupResponse)
async def create_group(group_data: schemas.GroupCreate, db: Session = Depends(database.get_db)):
    name = group_data.name.capitalize()
    new_group = models.Group(name=name, code=shortuuid.ShortUUID().random(length=8))
    db.add(new_group)
    db.commit()
    db.refresh(new_group)
    return new_group

@router.post("/join", response_model=schemas.GroupResponse)
async def join_group(group_data: schemas.GroupJoin, db: Session = Depends(database.get_db)):
    group = db.query(models.Group).filter(models.Group.code == group_data.code).first()
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    return group
