#!/usr/bin/env bash
if [ -z $BRANCH ]; then
  BRANCH=develop
fi

WORKDIR=/srv/django/web

cd $WORKDIR

git reset --hard HEAD~
git fetch origin
git checkout --track origin/$BRANCH
git pull git@github.com:AIright/web.git
docker build -t blog_base:latest ./deploy
docker-compose up -d

echo http://ec2-"$(curl -s http://checkip.amazonaws.com | sed 's/\./-/g')".eu-central-1.compute.amazonaws.com/
