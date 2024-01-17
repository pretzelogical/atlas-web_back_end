#!/bin/bash
# Attach to a docker container

docker container exec -it $1 /bin/bash
