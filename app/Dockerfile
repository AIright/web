# FROM python:3.8.1-alpine
FROM blog_base

WORKDIR /opt/app

COPY ./blog /opt/app/blog
COPY manage.py /opt/app/

CMD ["gunicorn","--bind",":8000","blog.wsgi"]
