#!/usr/bin/env bash
if [ -z $BRANCH ]; then
  BRANCH=develop
fi

WORKDIR=/opt/web

mkdir -p $WORKDIR && cd $WORKDIR

git reset --hard HEAD~
git clone git@github.com:AIright/web.git -b $BRANCH

docker build -t blog_base ./deploy

docker-compose up -d

echo http://ec2-"$(curl -s http://checkip.amazonaws.com | sed 's/\./-/g')".eu-central-1.compute.amazonaws.com/
