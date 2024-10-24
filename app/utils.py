import redis.asyncio as redis
from fastapi_limiter import FastAPILimiter

# Redis setup with error handling for rate limiting
async def setup_redis():
    try:
        redis_instance = redis.from_url("redis://localhost:6379", encoding="utf-8", decode_responses=True)
        await FastAPILimiter.init(redis_instance)
        print("Redis setup successful")
    except Exception as e:
        print(f"Failed to initialize Redis: {e}")
        # Handle more graceful fallbacks here if needed for production
