FROM python:3.8.1-alpine

WORKDIR /opt/app

COPY ./blog /opt/app/
COPY manage.py /opt/app/
COPY requirements.txt /opt/app/

RUN apk add --no-cache \
    dumb-init \
    mariadb-client \
    && pip install -r requirements.txt
CMD ["gunicorn","blog.wsgi"]
