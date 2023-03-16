FROM ubuntu:20.04

LABEL maintainer="Ozan Tokatli"
LABEL email="ozan.tokatli@gmail.com"

ARG DEBIAN_FRONTEND=noninteractive

# Change shell to bash
SHELL ["/bin/bash", "-c"]


# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip python3-numpy python3-scipy

# Workspace
RUN mkdir -p /workspace/packages
ENV WS /workspace
WORKDIR $WS/packages

# Install Kortex API (Python)
COPY ./libraries/kortex_api-2.5.0.post6-py3-none-any.whl .
RUN python3 -m pip install kortex_api-2.5.0.post6-py3-none-any.whl
