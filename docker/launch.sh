#!/bin/bash
GID=`id -g`
docker run -it --user "${UID}":"${GID}" -p 8888:8888 -v "${PWD}"/../app:/home/user/app --name=dash-example shantanugoel/dash-example-docker $@
