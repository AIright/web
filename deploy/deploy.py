#!/usr/env python3
import json
import os


# Read env file
with open('.env') as f:
    env = json.load(f)  # type: dict

# Set environment variables
for k, v in env.items():
    os.environ[k] = v

# Deploy
os.system('docker-compose build')
os.system('docker-compose up -d')
os.system('docker ps -a')
