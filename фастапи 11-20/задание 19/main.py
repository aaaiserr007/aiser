from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import List, Optional

class Note(BaseModel):
    id: int = Field(..., description="ID заметки", example=1)
    text: str = Field(..., description="Текст заметки", example="Пример заметки")

class NoteCreate(BaseModel):
    text: str = Field(..., description="Текст новой заметки", example="Новая заметка")

class ErrorResponse(BaseModel):
    detail: str = Field(..., description="Описание ошибки", example="Not found")

notes_db = [
    {"id": 1, "text": "Первая заметка"},
    {"id": 2, "text": "Вторая заметка"}
]

app = FastAPI(
    title="Notes API",
    description="API для управления заметками с расширенной документацией OpenAPI.",
    version="1.0.0",
    contact={
        "name": "API Support",
        "email": "support@example.com"
    }
)

@app.get(
    "/notes",
    response_model=List[Note],
    tags=["Notes"],
    summary="Получить список заметок",
    description="Возвращает все заметки.",
    responses={
        200: {
            "description": "Список заметок",
            "content": {
                "application/json": {
                    "example": [
                        {"id": 1, "text": "Первая заметка"},
                        {"id": 2, "text": "Вторая заметка"}
                    ]
                }
            }
        }
    }
)
def get_notes():
    return notes_db

@app.post(
    "/notes",
    response_model=Note,
    status_code=status.HTTP_201_CREATED,
    tags=["Notes"],
    summary="Создать новую заметку",
    description="Создаёт новую заметку и возвращает её.",
    responses={
        201: {
            "description": "Заметка создана",
            "content": {
                "application/json": {
                    "example": {"id": 3, "text": "Новая заметка"}
                }
            }
        },
        400: {
            "description": "Ошибка валидации",
            "model": ErrorResponse,
            "content": {
                "application/json": {
                    "example": {"detail": "Invalid data"}
                }
            }
        }
    }
)
def create_note(note: NoteCreate):
    new_id = max(n["id"] for n in notes_db) + 1 if notes_db else 1
    new_note = {"id": new_id, "text": note.text}
    notes_db.append(new_note)
    return new_note

@app.get(
    "/notes/{note_id}",
    response_model=Note,
    tags=["Notes"],
    summary="Получить заметку по ID",
    description="Возвращает заметку по её идентификатору.",
    responses={
        200: {
            "description": "Заметка найдена",
            "content": {
                "application/json": {
                    "example": {"id": 1, "text": "Первая заметка"}
                }
            }
        },
        404: {
            "description": "Заметка не найдена",
            "model": ErrorResponse,
            "content": {
                "application/json": {
                    "example": {"detail": "Not found"}
                }
            }
        }
    }
)
def get_note(note_id: int):
    for note in notes_db:
        if note["id"] == note_id:
            return note
    raise HTTPException(status_code=404, detail="Not found")

@app.delete(
    "/notes/{note_id}",
    response_model=ErrorResponse,
    tags=["Notes"],
    summary="Удалить заметку",
    description="Удаляет заметку по её идентификатору.",
    responses={
        200: {
            "description": "Заметка удалена",
            "content": {
                "application/json": {
                    "example": {"detail": "Deleted"}
                }
            }
        },
        404: {
            "description": "Заметка не найдена",
            "model": ErrorResponse,
            "content": {
                "application/json": {
                    "example": {"detail": "Not found"}
                }
            }
        }
    }
)
def delete_note(note_id: int):
    for i, note in enumerate(notes_db):
        if note["id"] == note_id:
            notes_db.pop(i)
            return {"detail": "Deleted"}
    raise HTTPException(status_code=404, detail="Not found") 