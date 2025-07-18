# Task 11: Celery + Redis + FastAPI + Docker Compose

## Описание
В этом задании реализуется система для выполнения длительных задач в фоне с помощью Celery и Redis. Пример — имитация отправки email.

## Сервисы
- FastAPI (backend)
- Redis (брокер для Celery)
- Celery Worker

## Запуск
1. Установите Docker и Docker Compose.
2. В папке `task_11` выполните:
   ```sh
   docker-compose up --build
   ```
3. Откройте FastAPI docs: http://localhost:8000/docs
4. Вызовите POST `/send-email` — получите быстрый ответ.
5. Проверьте логи celery_worker (в консоли docker-compose) — увидите выполнение задачи.

## Структура
- `main.py` — FastAPI приложение
- `celery_app.py` — конфиг Celery
- `tasks.py` — задачи Celery
- `docker-compose.yml` — инфраструктура 

Вот разбор и решение по вашей ошибке:

### 1. Предупреждение о `version`
```
the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion
```
Это просто предупреждение. В новых версиях Docker Compose можно убрать строку `version: '3.8'` из docker-compose.yml — это не критично и не мешает запуску.

---

### 2. Основная ошибка: unable to get image ... open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified.
Это значит, что Docker Desktop (или его Linux Engine) не запущен или не установлен.

**Причины:**
- Docker Desktop не запущен.
- Docker Desktop не установлен.
- Вы используете Windows, а Docker Desktop не настроен или не работает.

---

## Как исправить

1. **Проверьте, установлен ли Docker Desktop**
   - Откройте меню «Пуск» и найдите «Docker Desktop».
   - Если не установлен — скачайте и установите с [официального сайта Docker](https://www.docker.com/products/docker-desktop/).

2. **Запустите Docker Desktop**
   - Запустите приложение «Docker Desktop».
   - Дождитесь, пока появится статус «Docker is running» (или зелёная иконка в трее).

3. **Проверьте работу Docker в терминале**
   Откройте PowerShell или CMD и выполните:
   ```sh
   docker info
   ```
   Если всё работает, вы увидите информацию о Docker. Если нет — будет ошибка.

4. **Повторите запуск**
   После запуска Docker Desktop снова выполните:
   ```sh
   cd "C:\Users\HUAWEI\Desktop\fastapi 11-20\task_13"
   docker-compose up --build
   ```

---

### Если не помогает:
- Перезагрузите компьютер.
- Проверьте, что нет конфликтующих программ (например, WSL2, если не используется).
- Убедитесь, что используете актуальную версию Docker Desktop.

---

Если после этих шагов проблема останется — пришлите текст ошибки после запуска `docker info` и я помогу дальше! 