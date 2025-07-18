# Task 19: Улучшение OpenAPI-документации FastAPI

## Описание
В этом задании реализуется расширенная документация OpenAPI с помощью тегов, описаний, примеров, моделей ответов и общей информации о сервисе.

## Запуск
1. Установите Docker и Docker Compose.
2. В папке `task_19` выполните:
   ```sh
   docker-compose up --build
   ```
3. Откройте:
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## Структура
- `main.py` — FastAPI приложение с расширенной документацией
- `docker-compose.yml`, `Dockerfile`, `requirements.txt` — инфраструктура 