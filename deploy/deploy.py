#!/usr/bin/env python3
import json
from subprocess import check_call


# Read env file
with open('deploy/.env') as f:
    env = json.load(f)  # type: dict

# Deploy
check_call('docker-compose down', shell=True, env=env)
check_call('docker-compose build', shell=True, env=env)
check_call('docker-compose up -d', shell=True, env=env)
check_call('docker ps -a', shell=True)
check_call('docker exec -it blog ./manage.py collectstatic', shell=True)

# Don't forget to create user and grant them permissions manually
# Then make migrations:
# ./manage.py makemigrations blog
# ./manage.py migrate
