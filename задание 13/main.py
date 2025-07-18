import json
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import aioredis
from typing import List

app = FastAPI()

# Эмуляция "БД"
NOTES_DB = [
    {"id": 1, "text": "Первая заметка"},
    {"id": 2, "text": "Вторая заметка"}
]
REDIS_URL = "redis://redis:6379/0"
CACHE_KEY = "notes_cache"
CACHE_TTL = 30  # секунд

@app.on_event("startup")
async def startup():
    app.state.redis = await aioredis.create_redis_pool(REDIS_URL)

@app.on_event("shutdown")
async def shutdown():
    app.state.redis.close()
    await app.state.redis.wait_closed()

@app.get("/notes")
async def get_notes():
    redis = app.state.redis
    cached = await redis.get(CACHE_KEY)
    if cached:
        notes = json.loads(cached)
        return {"notes": notes, "source": "cache"}
    # Эмуляция задержки БД
    notes = NOTES_DB
    await redis.set(CACHE_KEY, json.dumps(notes), expire=CACHE_TTL)
    return {"notes": notes, "source": "db"}

@app.post("/notes")
async def add_note(text: str):
    new_id = max(n["id"] for n in NOTES_DB) + 1 if NOTES_DB else 1
    NOTES_DB.append({"id": new_id, "text": text})
    await app.state.redis.delete(CACHE_KEY)
    return {"id": new_id, "text": text}

@app.delete("/notes/{note_id}")
async def delete_note(note_id: int):
    global NOTES_DB
    NOTES_DB = [n for n in NOTES_DB if n["id"] != note_id]
    await app.state.redis.delete(CACHE_KEY)
    return {"result": "deleted"} 