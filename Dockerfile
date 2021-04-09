FROM python:3.8.5

WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn yatube_api.wsgi:application -b 0.0.0.0:8000
