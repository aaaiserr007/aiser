# Task 15: CI/CD с GitHub Actions

## Описание
В этом задании реализуется базовый CI/CD пайплайн с использованием GitHub Actions. Пайплайн автоматически запускает тесты и собирает Docker-образ при каждом push в main/master.

## Структура
- `.github/workflows/ci.yml` — workflow для GitHub Actions
- `main.py` — пример приложения
- `tests/test_sample.py` — пример теста
- `requirements.txt`, `Dockerfile`, `docker-compose.yml` — инфраструктура

## Проверка
1. Сделайте push в репозиторий на GitHub.
2. Перейдите во вкладку "Actions" — убедитесь, что workflow проходит успешно.
3. Измените код, снова сделайте push — убедитесь, что пайплайн снова проходит. 