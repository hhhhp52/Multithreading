FROM python:3.8.1
MAINTAINER Schnee Ruan <hhhhp52@gmail.com>
LABEL authors="Schnee"

COPY . /multithreading
WORKDIR /multithreading

CMD ["python3", "thread.py"]