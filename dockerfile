FROM python:3

ENV TERM xterm-256color

WORKDIR /usr/app/src

COPY . .

