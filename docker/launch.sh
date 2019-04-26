#!/bin/bash
GID=`id -g`
docker run --rm -it --user "${UID}":"${GID}" -p 8888:8888 -v "${PWD}"/../app:/home/user/app --name=dash-example shantanugoel/dash-example-docker $@
#docker run --rm -it -p 8888:8888 -v "${pwd}"/../app:/home/user/app --name=dash-example shantanugoel/dash-example-docker $@
