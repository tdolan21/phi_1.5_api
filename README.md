# Phi 1.5 API (Unoffical)

![Docker Build Status](https://img.shields.io/docker/build/tdolan21/phi_1.5_api)
![GitHub last commit](https://img.shields.io/github/last-commit/tdolan21/phi_1.5_api)
![PyTorch](https://img.shields.io/badge/PyTorch-1.9-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68-blue)
![License](https://img.shields.io/github/license/google/skia)

This API is implemented with FastAPI and PyTorch to allow an even lighter-weight usage of output from Microsoft's [phi-1.5](https://huggingface.co/microsoft/phi-1_5) model.


## Prerequisites

Before you pull the docker image you will need to install the Nvidia container toolkit and follow the steps available [here](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)

Once you have completed this step you can continue.

## Installation

The quickest way to use this API is to use:

```bash
docker pull miniagi/phi_1.5_api
docker run --rm --gpus all -p 8000:8000 --name phi_api miniagi/phi_1.5_api
```


## Build it yourself


```bash
git clone https://github.com/tdolan21/phi_1.5_api
cd phi_1.5_api
```

Use this command to build the image from the Dockerfile:

```bash
docker build -t phi_1.5_api .

```
Use this command to enter the container runtime from the docker enegine:

```bash
docker run --rm --gpus all -p 8000:8000 --name phi_api phi_1.5_api
```
Once you are in the container runtime you can launch the application like this:

```bash
uvicorn api:app --host 0.0.0.0 --port 8000
```

## Usage

Once the container is running you can access it in these places:

```
0.0.0.0:8000/
0.0.0.0:8000/docs
0.0.0.0:8000/phi
```
**'/'**: Returns "welcome to phi 1.5 api" to test connection
**'/docs'**: This endpoint is provided by FastAPI to test the endpoints manually
**'/phi'**: Expects a string (user input) and max_length integer that defaults to 200.


## Known Issues

The nvidia/cuda base image is needed to use your local gpu compute in the container. As a result, the torch install for gpu support must occur in the container launch because torch is wiped from the image even if has successfully built.

The main downfall of this is the perceived build time is longer. The torch install occurs when you launch the api, but it would need to happen in the dockerfile either way. I welcome any other solutions that allow for the app to build without entering interactive mode.