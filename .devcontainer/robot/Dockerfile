FROM ubuntu:18.04

LABEL maintainer="Ozan Tokatli"
LABEL email="ozan.tokatli@gmail.com"

ARG DEBIAN_FRONTEND=noninteractive

# Change shell to bash
SHELL ["/bin/bash", "-c"]

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip python3-numpy python3-scipy python3-zmq protobuf-compiler && \
    python3 -m pip install smooth-trajectory pyKinovaGen3

# Install Kortex API (Python)
RUN mkdir -p /external
COPY ./libraries/kortex_api-2.5.0.post6-py3-none-any.whl /external
RUN python3 -m pip install /external/kortex_api-2.5.0.post6-py3-none-any.whl

# Protobuf files
RUN mkdir -p /protobuf/proto && mkdir -p /protobuf/python
COPY /proto/kinovagen3.proto /protobuf/proto/

# Compile the proto file into python
RUN protoc -I=/protobuf/proto --python_out=/protobuf/python /protobuf/proto/kinovagen3.proto

# Workspace
RUN mkdir /workspace
WORKDIR /workspace
