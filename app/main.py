from fastapi import FastAPI
from .routers import groups, items  # Assuming you have items.py in routers too
from .utils import setup_redis

app = FastAPI()
@app.on_event("startup")
async def startup():
    await setup_redis()

app.include_router(groups.router, prefix="/groups", tags=["Groups"])
app.include_router(items.router, prefix="/items", tags=["Items"])

