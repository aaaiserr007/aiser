# Task 13: Кеширование с Redis и aioredis

## Описание
В этом задании реализуется кеширование часто запрашиваемых данных (например, заметок) с помощью Redis и aioredis. Кеш инвалидация происходит при изменении данных.

## Запуск
1. Установите Docker и Docker Compose.
2. В папке `task_13` выполните:
   ```sh
   docker-compose up --build
   ```
3. Откройте FastAPI docs: http://localhost:8000/docs
4. Проверьте работу кеша:
   - Первый GET /notes — данные из "БД" (эмулируется)
   - Второй GET /notes — данные из кеша
   - POST/PUT/DELETE /notes — инвалидация кеша

## Структура
- `main.py` — FastAPI приложение с кешированием
- `docker-compose.yml`, `Dockerfile`, `requirements.txt` — инфраструктура 