FROM postgres:latest

ENV POSTGRES_PASSWORD=ethyme_secret
ENV POSTGRES_USER=ethyme_user
ENV POSTGRES_DB=ethyme_db

VOLUME ethyme_volume:/var/lib/postgresql/data

WORKDIR /usr/bin/bash

# RUN postgres
RUN psql -h localhost -U eThyme_user

RUN create database timetable (id serial primary key, clockin DATE, clockout DATE, total int, descriptiong TEXT);

EXPOSE "5432"
