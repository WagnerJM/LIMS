# Hubertus

## todo
### app
- create admin check function
- speichern in der Datenbank vorbereiten von manage.py

~~ - flask_migrate zur __init__ Datei hinzufügen~~

## Notizen

https://www.revsys.com/tidbits/celery-and-django-and-docker-oh-my/


https://github.com/andymccurdy/redis-py
PUB/SUB

https://stackoverflow.com/questions/28982974/flask-restful-upload-image


## Installation

.env Datei erstellen

```
APP_SETTINGS=
FLASK_APP=
FLASK_ENV=
POSTGRES_USER=
POSTGRES_PW=
REDIS_PW=
DATABASE=
SECRET_KEY=
JWT_SECRET=

```

<code> mkdir data </code>

- Secret Key herstellen zb. über die python shell

<code>
import secrets

secrets.token_hex(32)
</code>

Anschließend Key rauskopieren und in .env Datei einfügen

- Change Titel in client/public/index.html


```
migrate cmd

flask db init -> initalisieren der Datenbank (beim ersten Mal notwending)

flask db migrate -> bei jeder Änderung machen

flask db upgrade -> bei jeder Änderung machen
```
