#!/usr/bin/env bash
# Run redis server and expose port 6379 (default redis port)

docker run -d -p 6379:6379 redis
