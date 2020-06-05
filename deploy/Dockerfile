FROM python:3.8.1-alpine

COPY requirements.txt /tmp

RUN apk add --no-cache mariadb-dev build-base \
    && pip install -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

CMD ["/bin/bash"]
