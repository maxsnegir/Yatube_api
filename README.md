# Проект "Api для Yatube"

### Описание

Предоставляет полноценный функционал приложения Yatube с помощью API

Документация представлена по адресу http://127.0.0.1/redoc

### Технологии

- Python 3.8
- Django 2.2.6 
- Django REST Framework 3.12.2
- Postgres 12
- Docker
- Nginx 1.19.3

### Копирование репозитория

*Через http протокол:*

```bash
git clone https://github.com/maxsnegir/Yatube_api.git
```

*Через ssh протокол:*

```bash
git clone git@github.com:maxsnegir/Yatube_api.git
```

## Запуск проекта

_Все команды должны выполняться в главной директории проекта._

1. Создайте файл **.env** со следующеми переменными окружения для работы с
   базой данных:

```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=admin # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
```

2. Убедитесь, что у вас
   установлен [Docker](https://www.docker.com/products/docker-desktop)
   и запустите проект командой:

```bash
docker-compose up 
```

3. Чтобы выполнить миграции, собрать статические файлы и создать
   суперпользователя, выполните:

```bash
docker-compose exec web python manage.py makemigrations --noinput
docker-compose exec web python manage.py migrate --noinput
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```

4. Чтобы заполнить базу тестовыми данными, выполните команду:

```bash
docker-compose exec web python manage.py loaddata fixtures.json
```
5. Проект запущен и доступен по адресу http://127.0.0.1
### Автор

[Максим Снегирёв](https://t.me/maxsneg)

 
