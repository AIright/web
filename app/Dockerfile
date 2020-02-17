FROM python:3.8.1-alpine

WORKDIR /opt/app

COPY * /opt/app/

RUN pip install -r requirements.txt

CMD ['gunicorn', 'blog.wsgi']
