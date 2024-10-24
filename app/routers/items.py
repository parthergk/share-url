from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi_limiter.depends import RateLimiter
from .. import models, schemas, database

router = APIRouter()

# Share content in a group
@router.post("/share", dependencies=[Depends(RateLimiter(times=100, seconds=60))])
async def share_content(content: schemas.ShareContent, db: Session = Depends(database.get_db)):
    group = db.query(models.Group).filter(models.Group.id == content.groupId).first()
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")

    # Check if the URL has already been shared
    url_exists = db.query(models.SharedItem).filter(
        models.SharedItem.group_id == group.id,
        models.SharedItem.url == content.url
    ).first()

    if url_exists:
        raise HTTPException(status_code=400, detail="This URL has already been shared.")

    # Create a new shared item
    shared_item = models.SharedItem(url=content.url, group_id=group.id)
    db.add(shared_item)
    db.commit()
    db.refresh(shared_item)

    return {"success": True, "item": shared_item}

# Retrieve shared items in a group
@router.get("/{group_id}/items", response_model=list[schemas.SharedItemResponse])
async def get_shared_items(group_id: int, db: Session = Depends(database.get_db)):
    group = db.query(models.Group).filter(models.Group.id == group_id).first()
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")

    return group.shared_items
