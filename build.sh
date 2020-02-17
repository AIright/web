#!/bin/bash
VERSION=$(git log | head -1 | grep -Eo '[0-9a-f]{8}$')
docker build ./app/ -t blog:${VERSION}