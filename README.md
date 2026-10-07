# task_manager

Тестовое задание из двух частей:

1. **Task Management API** — CRUD для задач на Django + Django REST Framework (`ModelViewSet` + `DefaultRouter`), SQLite.
2. **FastAPI-микросервис** (`FastAPI_app.py`) — асинхронно запрашивает данные пользователя из внешнего API [JSONPlaceholder](https://jsonplaceholder.typicode.com) через `httpx.AsyncClient` и возвращает их клиенту.

## Модель Task

- `title` — строка, до 100 символов;
- `description` — текст, необязательное поле;
- `completed` — булево значение, по умолчанию `False`.

## Установка

```bash
git clone https://github.com/andreimelneichuk/task_manager.git
cd task_manager
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Django API

```bash
python manage.py migrate
python manage.py runserver
```

Эндпоинты:

- `GET /api/tasks/` — список задач;
- `POST /api/tasks/` — создание задачи;
- `GET /api/tasks/{id}/` — одна задача;
- `PUT/PATCH /api/tasks/{id}/` — обновление;
- `DELETE /api/tasks/{id}/` — удаление.

Пример:

```bash
curl -X POST http://127.0.0.1:8000/api/tasks/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Новая задача", "description": "Описание задачи"}'
```

Тесты CRUD-операций (`tasks/tests.py`):

```bash
python manage.py test
```

## FastAPI-микросервис

```bash
uvicorn FastAPI_app:app --reload --port 8001
curl http://127.0.0.1:8001/user/1
```

Ответ: `{"user": {...}}` с данными пользователя из JSONPlaceholder.

Тест (выполняет реальный запрос к JSONPlaceholder):

```bash
pytest test_FastAPI_app.py
```
