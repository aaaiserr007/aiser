# Task 18: Rate Limiting с Redis и FastAPI Middleware

## Описание
В этом задании реализуется ограничение количества запросов от одного клиента за определённое время с помощью Redis и кастомного Middleware.

## Запуск
1. Установите Docker и Docker Compose.
2. В папке `task_18` выполните:
   ```sh
   docker-compose up --build
   ```
3. Откройте FastAPI docs: http://localhost:8000/docs
4. Проверьте ограничение запросов (например, через Postman или скрипт).

## Структура
- `main.py` — FastAPI приложение с RateLimiterMiddleware
- `middleware.py` — реализация middleware
- `config.py` — настройки лимита
- `docker-compose.yml`, `Dockerfile`, `requirements.txt` — инфраструктура 