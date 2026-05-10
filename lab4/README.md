# lab2.3

Этот репозиторий содержит два Django‑проекта:

* `edu_journal` – основной сайт (порт 8001 по умолчанию).
* `api_project` – REST‑сервис для статей (порт 8002).

При запуске приложения необходимо запускать оба сервера в отдельных консолях:

```powershell
# в корне workspace
venv\Scripts\activate.ps1
python manage.py runserver 8001
```

```powershell
# в папке api_project
cd api_project
..\venv\Scripts\activate.ps1
python manage.py runserver 8002
```

Адрес API используется в `journal/views.py` через настройку
`API_BASE_URL` (по умолчанию `http://127.0.0.1:8002`).

Сервер `edu_journal` перенаправляет запросы на API и при отсутствии
работающего бэкенда будет логировать 404 или ConnectionError; следите за
правильным запуском сервиса.