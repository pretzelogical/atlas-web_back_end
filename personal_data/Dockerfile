# For testing with SQL
FROM mariadb:latest

RUN apt-get update && apt-get install -y systemctl python3 python3-mysql.connector vim

ENV MARIADB_ROOT_PASSWORD=pass
ENV PERSONAL_DATA_DB_USERNAME=root
ENV PERSONAL_DATA_DB_PASSWORD=root
ENV PERSONAL_DATA_DB_HOST=localhost
ENV PERSONAL_DATA_DB_NAME=my_db

COPY ./main.sql /docker-entrypoint-initdb.d/

COPY ./filtered_logger.py /usr/src/myapp/

RUN systemctl status mariadb
# RUN python3 ./usr/src/myapp/filtered_logger.py
