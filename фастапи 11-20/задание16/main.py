from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from models import Base, Note
import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://testuser:testpass@db:5432/testdb"
)

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    # Можно создать таблицы (но лучше через Alembic)
    pass

@app.get("/notes")
async def get_notes():
    async with SessionLocal() as session:
        result = await session.execute(
            Note.__table__.select()
        )
        notes = result.fetchall()
        return [dict(row._mapping) for row in notes] 