# Task 14: Управление настройками через переменные окружения и Pydantic Settings

## Описание
В этом задании реализуется централизованное управление настройками приложения через переменные окружения и pydantic-settings. Все параметры берутся из .env или переменных окружения.

## Запуск
1. Установите Docker и Docker Compose.
2. В папке `task_14` выполните:
   ```sh
   docker-compose up --build
   ```
3. Откройте FastAPI docs: http://localhost:8000/docs

## Структура
- `main.py` — FastAPI приложение, использующее настройки
- `config.py` — класс BaseSettings
- `.env` — переменные окружения для локальной разработки
- `docker-compose.yml`, `Dockerfile`, `requirements.txt` — инфраструктура 