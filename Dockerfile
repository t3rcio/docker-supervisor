# syntax=docker/dockerfile:1
FROM python:3.9

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y supervisor
RUN mkdir -p /var/log/supervisor

WORKDIR /code
COPY . /code
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN mkdir logs

RUN supervisord -c /etc/supervisor/conf.d/supervisord.conf &

