# Task 17: Логирование и мониторинг с Prometheus

## Описание
В этом задании реализуется структурированное логирование (JSON) и мониторинг с помощью Prometheus. Приложение FastAPI логирует запросы, предоставляет /health и /metrics.

## Запуск
1. Установите Docker и Docker Compose.
2. В папке `task_17` выполните:
   ```sh
   docker-compose up --build
   ```
3. Откройте:
   - FastAPI docs: http://localhost:8000/docs
   - /health: http://localhost:8000/health
   - /metrics: http://localhost:8000/metrics
   - Prometheus UI: http://localhost:9090

## Структура
- `main.py` — FastAPI приложение с логированием и метриками
- `prometheus.yml` — конфиг Prometheus
- `docker-compose.yml`, `Dockerfile`, `requirements.txt` — инфраструктура 