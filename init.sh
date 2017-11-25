#!/usr/bin/env bash
sudo ln -s $PWD/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -s $PWD/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo ln -s $PWD/etc/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql start
# gunicorn -c hello.py wsgi.py
