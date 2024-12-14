FROM localhost:5000/nvidia-cuda121-win64:mini-0.0.2 AS base

ARG DEBIAN_FRONTEND=noninteractive
ARG BASE_MODEL

ENV BASE_MODEL=$BASE_MODEL

WORKDIR /workspace

# Install linux packages
# g++ required to build 'tflite_support' and 'lap' packages, libusb-1.0-0 required for 'tflite_support' package
# libsm6 required by libqxcb to create QT-based windows for visualization; set 'QT_DEBUG_PLUGINS=1' to test in docker
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc git zip unzip wget curl htop libgl1 libglib2.0-0 libpython3-dev gnupg g++ libusb-1.0-0 libsm6 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN python3.10 -m pip install -r requirements.txt
COPY . .

ENTRYPOINT [ "python3.10"]
