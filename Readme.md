**Running several services in a single container with Supervisor**

It is possible to run muiltiple services in a single container with supervisor

```dockerfile
#Dockerfile
FROM python:3.9

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y supervisor
RUN mkdir -p /var/log/supervisor

WORKDIR /code
COPY . /code
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN mkdir logs

RUN supervisord -c /etc/supervisor/conf.d/supervisord.conf &
```

```yml
#docker-compose.yml
version: "3.9"

services:
   supervisor:
      build: .
      restart: always
      command: /usr/bin/supervisord
      volumes:
         - .:/code
      
```

Running with:

```shell
user@user-pc:~$ docker-compose -f docker-compose.yml -up
```

Look at the log file to confirm the services running:

```shell
user@user-pc:~$ tail -f out1.log
(...)
user@user-pc:~$ tail -f out2.log
```

**References:**

[Run multiple services in a container | Docker Documentation](https://docs.docker.com/config/containers/multi-service_container/)

[Docker Tutorial =&gt; Dockerfile + supervisord.conf](https://riptutorial.com/docker/example/14132/dockerfile-plus-supervisord-conf)


