from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

# Custom exception handler for FastAPI
async def custom_exception_handler(request: Request, exc: Exception):
    # Handle uncaught exceptions
    return JSONResponse(
        status_code=500,
        content={"message": "An internal error occurred. Please try again later.", "detail": str(exc)},
    )

# HTTPException handler for better error responses
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )
