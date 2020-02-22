# FROM python:3.8.1-alpine
FROM blog_base

WORKDIR /opt/app

COPY ./blog /opt/app/blog
COPY manage.py /opt/app/
COPY requirements.txt /opt/app/

RUN apk add --no-cache mariadb-dev build-base \
    && pip install -r requirements.txt
CMD ["gunicorn","--bind",":8000","blog.wsgi"]
