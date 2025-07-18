from fastapi import FastAPI
import aioredis
from config import REDIS_URL
from middleware import RateLimiterMiddleware

app = FastAPI()

@app.on_event("startup")
async def startup():
    app.state.redis = await aioredis.create_redis_pool(REDIS_URL)
    app.add_middleware(RateLimiterMiddleware, redis=app.state.redis)

@app.on_event("shutdown")
async def shutdown():
    app.state.redis.close()
    await app.state.redis.wait_closed()

@app.get("/")
async def root():
    return {"message": "Hello, rate limit!"} 