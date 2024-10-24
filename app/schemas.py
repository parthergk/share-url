from pydantic import BaseModel
from datetime import datetime
from typing import List

class GroupCreate(BaseModel):
    name: str

class GroupJoin(BaseModel):
    code: str

class ShareContent(BaseModel):
    groupId: int
    url: str

class SharedItemResponse(BaseModel):
    url: str
    shared_at: datetime

    class Config:
        from_attributes = True

class GroupResponse(BaseModel):
    name: str
    code: str
    shared_items: List[SharedItemResponse]

    class Config:
        from_attributes = True
