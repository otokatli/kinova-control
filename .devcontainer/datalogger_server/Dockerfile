FROM ubuntu:20.04

LABEL maintainer="Ozan Tokatli"
LABEL email="ozan.tokatli@gmail.com"

ARG DEBIAN_FRONTEND=noninteractive

# Change shell to bash
SHELL ["/bin/bash", "-c"]

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-zmq python3-protobuf protobuf-compiler

# Workspace
RUN mkdir -p /workspace/packages
ENV WS /workspace
WORKDIR $WS

COPY server.py $WS

RUN mkdir $WS/proto
COPY ./proto/kinovagen3.proto $WS/proto

RUN protoc -I=$WS/proto --python_out=. kinovagen3.proto

CMD [ "/usr/bin/python3", "server.py" ]
