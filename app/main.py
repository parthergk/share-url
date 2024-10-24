from fastapi import FastAPI
from app.routers import groups, items  # Corrected relative imports to absolute imports
from app.utils import setup_redis  # Assuming the utils.py file has setup_redis function
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Redis setup on startup
@app.on_event("startup")
async def startup():
    await setup_redis()

# Middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (you can restrict this in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Include Routers
app.include_router(groups.router, prefix="/groups", tags=["Groups"])
app.include_router(items.router, prefix="/items", tags=["Items"])
