FROM ubuntu:18.04

LABEL maintainer="Ozan Tokatli"
LABEL email="ozan.tokatli@gmail.com"

ARG DEBIAN_FRONTEND=noninteractive

# Change shell to bash
SHELL ["/bin/bash", "-c"]

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    cmake build-essential libeigen3-dev python3-pip python3-numpy python3-scipy python3-zmq protobuf-compiler && \
    python3 -m pip install smooth-trajectory pyKinovaGen3


RUN mkdir /external
COPY ./libraries/kortex /external/kortex
COPY ./libraries/kortex_api-2.5.0.post6-py3-none-any.whl /external
RUN mkdir build
WORKDIR /external/kortex/api_cpp/examples/build
RUN cmake .. -DUSE_CONAN=OFF -DCMAKE_BUILD_TYPE=release && make
RUN python3 -m pip install /external/kortex_api-2.5.0.post6-py3-none-any.whl

# Protobuf files
RUN mkdir -p /protobuf/proto && mkdir -p /protobuf/python && mkdir -p /protobuf/cpp
COPY /proto/kinovagen3.proto /protobuf/proto/

# Compile the proto file into python and c++
RUN protoc -I=/protobuf/proto --python_out=/protobuf/python /protobuf/proto/kinovagen3.proto
RUN protoc -I=/protobuf/proto --cpp_out=/protobuf/cpp /protobuf/proto/kinovagen3.proto

# Workspace
RUN mkdir /workspace
WORKDIR /workspace
