FROM postgis/postgis:11-2.5-alpine

RUN apk update && apk add --no-cache curl vim wget bash

COPY ./db/3_dataheader_schema.sql /docker-entrypoint-initdb.d/3_dataheader_schema.sql

COPY ./db/4_dataheader_data.sql /docker-entrypoint-initdb.d/4_dataheader_data.sql
