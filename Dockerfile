FROM ubuntu:latest
LABEL authors="tito"

ENTRYPOINT ["top", "-b"]