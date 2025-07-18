from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from fastapi import HTTPException
from config import RATE_LIMIT, RATE_LIMIT_WINDOW
import time

class RateLimiterMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, redis):
        super().__init__(app)
        self.redis = redis

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        key = f"ratelimit:{client_ip}"
        count = await self.redis.incr(key)
        if count == 1:
            await self.redis.expire(key, RATE_LIMIT_WINDOW)
        if count > RATE_LIMIT:
            ttl = await self.redis.ttl(key)
            raise HTTPException(status_code=429, detail=f"Rate limit exceeded. Try again in {ttl} seconds.")
        response = await call_next(request)
        return response 