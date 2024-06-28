### Проект «API для Yatube»
Данный проект - это REST API для проекта Yatube.

Через этот интерфейс могут работать мобильное приложение или чат-бот;

данные через этот API можно передавать и на фронтенд.
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Pr1ority/api_final_yatube
```

```
cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
### Примеры запросов к API

* /api/v1/posts/ - получение публикаций

* /api/v1/posts/{post_id}/comments - добавление комментария

* /api/v1/groups - список сообществ

* /api/v1/follow - подписка

* /api/v1/jwt/create/ - получение JWT-токена


