#!/bin/bash
# build and run test SQL/Python image

docker build -t mdb:task3 .
docker run mdb:task3
