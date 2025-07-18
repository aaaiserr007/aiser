# Task 12: FastAPI WebSocket Chat

## Описание
В этом задании реализуется базовый механизм обмена сообщениями в реальном времени через WebSocket.

## Запуск
1. Установите Docker и Docker Compose.
2. В папке `task_12` выполните:
   ```sh
   docker-compose up --build
   ```
3. Откройте FastAPI docs: http://localhost:8000/docs (для проверки API)
4. Для теста WebSocket используйте Postman или HTML-страницу из этого репозитория (`test_client.html`).

## Структура
- `main.py` — FastAPI приложение с WebSocket
- `connection_manager.py` — менеджер соединений
- `docker-compose.yml`, `Dockerfile`, `requirements.txt` — инфраструктура
- `test_client.html` — пример клиента для теста 