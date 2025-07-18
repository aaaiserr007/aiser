# Task 16: Alembic + SQLAlchemy + FastAPI

## Описание
В этом задании реализуется управление миграциями схемы БД с помощью Alembic и SQLAlchemy (async). Пример — создание таблицы notes и миграции.

## Запуск
1. Установите Docker и Docker Compose.
2. В папке `task_16` выполните:
   ```sh
   docker-compose up --build
   ```
3. Для работы с миграциями:
   - `alembic revision --autogenerate -m "init"` — создать миграцию
   - `alembic upgrade head` — применить миграцию
   - `alembic downgrade -1` — откатить миграцию

## Структура
- `main.py` — FastAPI приложение
- `models.py` — SQLAlchemy модели
- `alembic/` — миграции Alembic
- `alembic.ini` — конфиг Alembic
- `docker-compose.yml`, `Dockerfile`, `requirements.txt` — инфраструктура 