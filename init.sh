#!/usr/bin/env bash
sudo read -p "Enter Your Homedir: " homedir
sudo ln -s $homedir/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -s $homedir/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo ln -s $homedir/etc/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql start
# gunicorn -c hello.py wsgi.py
