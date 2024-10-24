from fastapi import FastAPI
from app.routers import groups, items
from app.utils import setup_redis
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Redis setup on startup
@app.on_event("startup")
async def startup():
    await setup_redis()

# Middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["chrome-extension://dbjdlhhkkdnnahcobbmnnjikkmmdnpgn"],  # Add the Chrome extension ID here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(groups.router, prefix="/groups", tags=["Groups"])
app.include_router(items.router, prefix="/items", tags=["Items"])
